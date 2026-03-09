TOP_8 = """
query TournamentTop8($page: Int!, $perPage: Int!, $tournamentName: String!, $stateCode: String!) {
  tournaments(
    query: {perPage: $perPage, page: $page, filter: {name: $tournamentName, addrState: $stateCode}, sortBy: "startAt desc"}
  ) {
    pageInfo {
      totalPages
    }
    nodes {
      events {
        videogame {
          name
        }
        standings(query: {perPage: 8}) {
          nodes {
            player {
              gamerTag
            }
            standing
          }
        }
      }
    }
  }
}
"""

HEADCOUNT = """
query TournamentHeadCount($page: Int!, $perPage: Int!, $tournamentName: String, $stateCode: String) {
  tournaments(
    query: {perPage: $perPage, page: $page, filter: {name: $tournamentName, addrState: $stateCode}, sortBy: "startAt desc"}
  ) {
    pageInfo {
      totalPages
    }
    nodes {
      events {
        videogame {
          name
        }
        entrants(query: {perPage: 50}) {
          nodes {
            participants {
              gamerTag
            }
          }
        }
      }
    }
  }
}
"""

USERINFO = """
query TournamentGetUser($tournamentName: String, $stateCode: String, $tag: String) {
  tournaments(
    query: {perPage: 1, sortBy: "startAt desc", filter: {name: $tournamentName, addrState: $stateCode}}
  ) {
    nodes {
      name
      events {
        name
        entrants(query: {filter: {name: $tag}, perPage: 1}) {
          nodes {
            participants {
              gamerTag
              player {
                user {
                  name
                  bio
                  genderPronoun
                  birthday
                }
              }
            }
          }
        }
      }
    }
  }
}
"""