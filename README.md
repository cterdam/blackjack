# blackjack

Benchmark Blackjack strategies.

## Intro

Use `Game` class to initialize a game.
Game runs should write a log of exact proceedings of the game to file.

## Testing

Simply run `pytest` in the root directory.

## Contributing

- Branch off and submit Pull Request to `main` when feature is complete.
- Write extensive test cases.
- Currently, we only have some infrastucture classes: `Card`, `Deck`, `Hand`,
  etc.
- TODO:
  - Short-term:
    - Add test case for `Hand` to make sure it's using different objects
      internally. (E.g. if you initialize it with a list then change the list
      this shouln't influence the Hand)
    - Add `str` and `repr` for `Hand` and add test cases
    - Add `explode` method for `Hand` which will create a separate hand from
      each card in hand
  - Long-term:
    - Add remaining config params in `GameConfig`
    - Add `Dealer` class, and implement S17 and H17 dealers
    - Add `Player` class, and implement some player strategies
    - Add `Game` class
