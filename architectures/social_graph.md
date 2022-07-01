# Social Graph

## Resources

* [Design Data Structures for a Social Graph](https://www.geeksforgeeks.org/design-data-structures-for-a-very-large-social-network-like-facebook-or-linkedln/)
* [System Design Primer](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/social_graph)

## Constraints

* 100M users
* Assume on average users have 50 friends
* 1 billion friend searches per month
* 300ms latency
* Traffic is not evenly distributed
* Graph data won't fit on a single machine
* Graph edges are un-waited


## Napkin Math


### Storage
* Uint32 Max: 4294967295
* Uint64 Max: 18446744073709551615

Uint32 gives room to space over our user estimate.

Graph Storage:
* Storage per user = (Number of friends * Uint32)
* Total graph storage = (Num users * Storage Per User)

Project Graph Storage = 300,000,000 * (100 * 32) =  960000000000 bits = ~ 120gb

## Database Schema

* User table
  * id: int32
  
* Connections
  * id: int32
  * connection_id: int32

## Graph Search Algorithm

Consider utilizing a Graph database which would simplify this like Neo4J. But if that's not an 
option we will have to build our own graph search.

First we need to store edges between users in an associations table, i.e. something like:

| user_name | connection |
| --------- | ---------- |
| joe | bill | 
| jane | bill |
| tim | alpert |
| jill | bill |
| jill | alpert |

* Use BFS or bi-directional BFS (start at user and start at target) and note when they collide.
* Don't use DFS since it will find a path but not necessarily the shortest path, 
additionally it would be very inefficient, two users could be very closely connected but DFS 
  could have to go down many trees to discover the connection.
* We need to track which individuals have been visited to prevent cycles using a hash table.

### How Performant is a BFS solution?

First lets simplify by calculating based on a common friend.

Suppose:

* Every person has k friends and Source S and Destination D have a friend C in common.
1. Traditional breadth-first search from S to D: We go through roughly k+k*k nodes: each of S’s k friends, and then each of their k friends.
2. Bidirectional breadth-first search: We go through 2k nodes: each of S’s k friends and each of D’s k friends. Of course, 2k is much less than k+k*k.
* Generalizing this to a path of length q, we have this:
    * BFS: O(kq)
    * Bidirectional BFS: 0( kq/2 + kq/2), which is just 0( kq/2)

If we imagine a path like A->B->C->D->E where each person has 100 friends, this is a big difference. 
BFS will require looking at 100 million (1004) nodes. A bidirectional BFS will require looking at 
only 20,000 nodes (2 x 1002).

## Architecture

[Lucid Chart](https://lucid.app/lucidchart/invitations/accept/inv_e98b4c26-69d5-4dee-ba64-631782c72419?viewport_loc=-11%2C-11%2C1608%2C1343%2C0_0)
