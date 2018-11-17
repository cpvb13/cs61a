"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    #return min( [distance(centroid,location) for centroid in centroids ] , key=lambda x:x )
    return min( centroids, key=lambda centroid:distance(location,centroid) )
    # for i in range(len(centroids)): #for each list in centroids
    #     current_dist=distance(centroids[i],location) #find the distance
    #     if i ==0: #set default min,index
    #         min_dist,index = current_dist,i
    #     elif current_dist<min_dist:
    #         min_dist,index = current_dist,i
    # return centroids[index]
    # END Question 3


def group_by_first(pairs):
    """Return a list of lists that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)  # Values from pairs that start with 1, 3, and 2 respectively
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    pairs = list()

    # find the closest centeroid for each restaurant
    for restaurant in restaurants:
        closest_cent = find_closest(restaurant_location(restaurant), centroids)
        pairs.append([closest_cent,restaurant]) #x in pair should be closest centeroid, y shoiuld be restaurant
    
    return group_by_first(pairs) #[  [0,0 closest centeroid], restaurant] #the length is # of restaurants ]
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    central_lon = mean([restaurant_location(restaurant)[0] for restaurant in cluster])
    central_lat = mean([restaurant_location(restaurant)[1] for restaurant in cluster])
    return [central_lon,central_lat]

#using the k-means algorithm groups the restaurants into k clusters by location.

#STEPS
#What is the first step of the k-means algorithm?

#1) Randomly initialize k centroids.
#2) Create a cluster for each centroid consisting of all elements closest to that centroid.
#3) Find the centroid (average position) of each cluster.

def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0

    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        #Group restaurants into clusters
        restaurant_cluster = group_by_centroid(restaurants,old_centroids) #each cluster contains all restaurants closest to a particular centroid in centroids.
    
        #Update centroids to contain the true centroid 
        centroids = [find_centroid(cluster) for cluster in restaurant_cluster]
        #(i.e. average location) for each cluster.
        n += 1
    
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    xs = [feature_fn(r) for r in restaurants]
    ys = [user_rating(user, restaurant_name(r)) for r in restaurants]

    # BEGIN Question 7
    S_xx= sum([((x - mean(xs))**2) for x in xs])#Sxx = Σi (xi - mean(x))^2
    S_yy= sum([pow(y - mean(ys),2) for y in ys]) #Syy = Σi (yi - mean(y))&2
    S_xy=  sum([((x - mean(xs))*(y - mean(ys))) for x,y in zip(xs, ys)])#Sxy = Σi (xi - mean(x)) (yi - mean(y))
    b=S_xy / S_xx
    a=mean(ys) - b * mean(xs)
    r_squared = (S_xy*S_xy) / (S_xx*S_yy)
    #print("check",S_xx,S_yy,S_xy,a,b,r_squared)
    # END Question 7

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 8
    predictor=[find_predictor(user, reviewed, f) for f in feature_fns]
    fn = max(predictor,key=lambda x:x[1])
    return fn[0]


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    reviewed_names = [restaurant_name(r) for r in reviewed] 
    #print(predictor,"\n",reviewed,"\n",reviewed_names)
    # BEGIN Question 9
    rest = {}
    for r in restaurants:
        #print(restaurant_name(r))
        if restaurant_name(r) in reviewed_names: 
            #print("yes")
            rest[restaurant_name(r)]=int(user_rating(user, restaurant_name(r))) #restaurant name is key, user value int
        else:
            rest[restaurant_name(r)]=predictor(r)  #restaurant name is key, predicted value decimal
    return rest
    # END Question 9




def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    return [r for r in restaurants if query in restaurant_categories(r)]
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)