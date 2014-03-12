Progressive Enhancement is a cornerstone of web development but when people talk about it they are normally talking about JavaScript, if CSS is included then it's normally in reference to cosmetic enhancements.  Here's how I extend this principle deeper into CSS and layer enhancements on a larger scale, taking advantage of the <abbr title="cascading">C</abbr> in CSS.

## Baseline presentation

Start with a baseline presentation as the main body of your CSS file (i.e. no media queries).  This should include resets, colours, typography and core elements of the site.  At this stage the layout should be minimal and strictly linear - however tempted you might be, <em>do not</em> include floats or positioning at this stage.  This is the layout that older browsers that do not support media queries will receive, this is sometimes referred to by the maxim: "The absence of media queries is the first media query."

## Narrow Screen

This is where we have our first media query and is used to enhance the presentation for browsers that support media queries. We use a media query of <code class="code">@media <b>only</b> all</code> to target these browsers.

As we now know the browser has a reasonably modern CSS engine and can be relied on to handle most layout instructions corrects we can now start using floats and positioning to move away from the strictly linear baseline presentation.  This is what you would typically think of as your first mobile layout for smartphones.

## Layered Media Queries

I'm not going to say too much about this as it is one of the cornerstones of responsive design - use the code within the media queries to build out your layouts to adapt to screen size or other signal.  Pay particular attention to how declarations override each other and pay attention to the 'reset' value of CSS properties as they differ.
