# Builder
- When construction gets a little bit too complicated

## Motivation
- Some objects are simple and can be created in a single initializer call
- Other objects require a lot of ceremony to create
- Having an object with 10+ initialize arguments is not productive
    - Instead, opt for piecewise construction
- The Builder provides an API for constructing an object step-by-step

### Formal Definition
Builder - When piecewise object construction is complicated, provide an API for doing it succinctly.