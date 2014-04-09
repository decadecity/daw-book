# Dealing with very small screens
With the increasing availability of wearable devices that include a web browser we will have to make sure we are coping with devices with a smaller width screen than 320px, which is the most common size for mobiles.

## Mobile first
The "mobile first" philosophy encourages us to start our implementation with mobile as that is the most constrained environment. It can therefore be tempting to consider the very small screens as the starting point as they are even more constrained.  However, although there are devices out there that have a smaller viewport than 320px they are in the minority so it is safe to assume 320px as the smallest **common** viewport. This means that we can continue to use the layout and typography of this viewport for our baseline presentation as this is what will be presented to devices that don't support media queries.

This baseline presentation is the main reason we don't start with the smallest viewports, we need a reliable starting point from which to enhance. We are treating support for very small screens as an enhancement rather than the default.

Normally when we build up from the baseline we use `min-width` media queries to layer on new styles as the viewport gets progressively wider, but for the narrow screens we need to use a `max-width` media query that will get layered on as the screen gets smaller.

<pre class="code"><code>body { // Reliable baseline.
  font-size: 100%;
}
@media all and (max-width:13.75em) { // Very small screens.
  body {
    font-size: 75%;
  }
}
@media all and (min-width:60em) { // Very large screens.
  body {
    font-size: 125%;
  }
}</code></pre>

If the layout has been built using ems for fixed dimensions (as opposed to pixels) then this has the additional benefit that it will scale down proportionally with the base font meaning it will adjust to better fit the very small screens with no additional changes.

## Knowing when to stop
As the readability of text degrades rapidly on smaller screens it might be tempting to optimise for smaller and smaller screens but at some point there will come a point where there simply isn't enough space to show any useful length of text.

Ultimately we have to rely on device makers to set the combination of screen size and pixel density that is most appropriate for their devices and accept that it's not our problem when they don't.
