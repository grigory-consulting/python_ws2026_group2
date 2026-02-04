



1. user id | item id | rating | timestamp 


Goal: 
        Recommend(user_id) -> item_id (maybe multiple item_ids, e.g. top-10)




        | Movie 1 | Movie 2 | Movie 3| .... | Movie N |
user1 = |  rating |    0    |  rating| .....|  0      |
user2 = |   0     |  rating | rating | .....|  0      |

movie1 = | user1 | user2 | ....  
         |   0   |  4    |
movie2 = | user1 | user2 | ....  
         |   2   |  5    |


distance(movie1, movie2) < threshold -> movie2 is similar to movie1