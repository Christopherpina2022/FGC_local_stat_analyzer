TOP_8 = """
query TournamentTop8($page: Int!) {
  tournaments(
    query: {perPage: 30, page: $page, filter: {name: "Crossover", addrState: "KS"}, sortBy: "startAt desc"}
  ) {
    pageInfo {
      totalPages
    }
    nodes {
      name
      slug
      events {
        name
        standings(query: {perPage: 8}) {
          nodes {
            player {
              gamerTag
              id
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
query TournamentHeadCount($page: Int!) {
  tournaments(
    query: {perPage: 30, page: $page, filter: {name: "Crossover", addrState: "KS"}, sortBy: "startAt desc"}
  ) {
    pageInfo {
      totalPages
    }
    nodes {
      name
      slug
      events {
        name
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