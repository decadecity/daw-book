# CSS

  * Baseline presentation
  * Media queries
  * Interaction optimisations

Like HTML, CSS has progressive enhancement built in - browsers will ignore things they don't understand. Again, providing we get the basics right, we can use advanced features provided we don't rely on them.

## Baseline presentation

  * Colours, typography, backgrounds, borders, etc.
  * Linear layout - no floats.
  * Basic interactions - no hover.

Your baseline presentation is the core elements of the CSS.  It should contain the basic style elements of your site such as the colours, typography, backgrounds, borders and the like.

The baseline layout should be completely linear with everything 100% width.  Don't use any floats at this stage as some legacy browsers don't handle floats and other layout styles very reliably.

Don't add any interaction enhancements at this point - specifically no hovers.

The site's not going to look very inspiring at this point, it's just one long list of branded content - not much different to the unstyled HTML.  However, this is exactly what we want - it's a baseline presentation that any browser with CSS support will be able to handle.

## Media Queries

  * Layout solution
  * Media query support: <code>@media only all</code>
  * Not just width

It's important to remember that media queries and responsive design are not a silver bullet to cross device compatibility.  They are a layout solution.

Layout is now probably the best understood section of building device agnostic web sites thanks to Responsive Design. What often gets lost is that Responsive Design is a layout solution - it is not a device solution. It's very tempting to look at certain screen widths and label them as devices: 320 is mobile, 768 is tablet and 1024 is desktop. Screen size to device class mapping was never that really a good assumption but as more and more form factors are coming on to the market it's becoming harmful.

We can detect for media query support with `@media only all`.

This is essentially our "cutting the mustard" test for good CSS support so, as we have a reliable baseline, we can start applying layout CSS and be fairly confident that it will be supported.

Don't forget that there are more media queries than just width.  For example height can be very useful to compress vertical whitespace for small screens in landscape orientation - such as Google Glass.

## Interaction optimisations
As different screen sizes require different layout requirements, different interface methods require different interface requirements.

  * Sequential (keyboard)
  * Direct (touch)
  * Location aware (hover)
  * Ambient / Passive (sensors)

There is a hierarchy of interactions.  Sequential navigation where you move from one item to the next in sequence is the baseline, this is normally keyboard navigation but that also includes things like game controllers.  The key to sequential interaction is keeping the user informed of where the current focus of interaction is.

Direct interaction uses the same interaction points as sequential but in this case they will be activated in isolation.  This is exemplified by touch interactions and is probably the easiest and mode of interaction to deal with.

Location aware interactions know where the point of interaction is before it is activated.  The mouse is the main example of this and it allows us to use hover states.  However, as this is further up the hierarchy you can't use this to present information not available to sequential and direct interactions.

At the bottom of the hierarchy we have ambient or passive interactions such as information from sensors such as location and network.  This is still a very new area and should be used with caution as they don't express a conscious desire for interaction.
