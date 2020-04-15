So, my idea is to create an API for countries, cities in historical perspective. Not only for the current year.
We can start doing this for one country, for example, Poland. Then do it for several major countries and then we can do a Medium article about it.

Country basic info:

- code 2
- code 3
- name
- population
- some ratings
- source
- cities

City basic info:

- code 2
- code 3
- name
- population
- source
- some ratings

I would like also to add information by year. Especially, it can be useful for some economical values.

Examples of the requests:

- `GET /api/v1/countries` (pagination)
- `GET /api/v1/country/pl`
- `GET /api/v1/country/pl/year/2020`
- `GET /api/v1/country/pl/cities` (pagination)
- `GET /api/v1/country/pl/city/krakow`
- `GET /api/v1/country/pl/city/krakow/year/2020`

Example of experiment APIs:

- `GET /api/experimental/counties/pl/economics`
