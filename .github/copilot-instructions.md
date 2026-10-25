# Project Guidance

- Keep the calculator page usable as a local static HTML file; use Gunicorn only for the Render WSGI service.
- Preserve the `window.conversionCalculator` API and its documented methods.
- Mass-to-volume conversions require an explicit density in kg/L; never present the default 0.804 kg/L as universal.
- Liters convert directly using US liquid gallons (3.785411784 liters per gallon).
- Keep the interface accessible, responsive, and validated for non-negative finite amounts and positive finite densities.
