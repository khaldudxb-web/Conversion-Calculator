# US Gallon Conversion Calculator

A browser-based HTML calculator for converting metric tons, liters, pounds, and kilograms to US liquid gallons. A small WSGI app serves the page on Render.

## Use

Open `index.html` directly in a browser, or run the WSGI app with `gunicorn your_application.wsgi:application`. Choose the input unit, enter a non-negative amount, and set the density in kg/L for mass conversions. The default density is 0.804 kg/L and is material-dependent. Liters convert directly and do not use density.

## JavaScript API

The page exposes `window.conversionCalculator` with these methods:

- `convertMetricTonsToUSGallons(metricTons, densityKgPerLiter = 0.804)`
- `convertLitersToUSGallons(liters)`
- `convertPoundsToUSGallons(pounds, densityKgPerLiter = 0.804)`
- `convertKilogramsToUSGallons(kilograms, densityKgPerLiter = 0.804)`

Methods return a number and throw `RangeError` for invalid amounts or densities. Mass conversions require a positive density in kilograms per liter. The calculator page remains usable as a local static file; Gunicorn is required only to run the Render WSGI service.
