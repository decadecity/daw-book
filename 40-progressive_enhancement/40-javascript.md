# JavaScript
  * No JavaScript
  * Feature detection
  * Cutting the mustard

Whilst JavaScript used to be used to provide small dynamic enhancements it's increasingly used to provide core functionality.  Unlike HTML and CSS, JavaScript is not fault tolerant.  If you include something in JavaScript that the browser does not understand it will come to a stop.  This means we need more robust techniques for enhancement.

## No JavaScript

  * Core content is accessible
  * Use JS to add a CSS hook
  * Use CSS hook to set initial presentation for enhanced functionality

Whilst it's easy to assume that JavaScript is everywhere these days, JavaScript support varies significantly between browsers and, as we did with HTML and CSS, we're going to be starting with a safe baseline and enhancing.  With JavaScript the safest baseline is when it's not present.

You don't have to have all your functionality replicated when JavaScript is disabled but your core content and any functionality required to access that should be available.

Before you declare any CSS in your page use some inline JavaScript to add a class to the HTML element.  This is really simple and can be done in one line.  Once you have the CSS hook you can then set the initial presentation for enhanced functionality - such as hiding everything in an expandable menu.

What you should be aiming for is being able to complete the basics - for example adding a product to a shopping cart and then checking out. This is going to be a lot more clunky than with JavaScript enabled and there's no reason to spend too much time optimising this.  Now, when (not if) when JavaScript breaks or otherwise isn't available, your users are still able to use your site.

## Feature Detection

  * Enhance functionality using feature if present
  * Polyfill missing feature
  * Fall back on non JavaScript functionality

Whilst browsers will ignore HTML or CSS they don't recognise, if you try to use JavaScript they don't recognise they'll throw an error.  To avoid this we need to detect if a feature is supported before using it.

The basic formulation for feature detection is to check for the presence of the feature in it's container - frequently `document` or `window`.  There are exceptions and it's different for HTML features but the idea is the same - you are detecting whether the feature you want to use is supported in the browser.

If you know the feature is supported you can then enhance using that feature.  If the feature isn't supported then you can either pollyfill to emulate the missing feature or fall back to the non JavaScript functionality.

<a href="http://remysharp.com/2010/10/08/what-is-a-polyfill/">Pollyfilling functionality</a> is tempting so it's very easy to end up with a lot of code doing this.  This code can be hard to maintain and test so, for each pollyfill, you should thoroughly examine if the feature you want to use really is important enough to warrant that investment of time.

So if we're not pollyfilling this missing JavaScript functionality what are we going to do?  Because we have started with a baseline that  core functionality is available without JavaScript we don't have to do anything - the cor

## Cutting the mustard

  * Feature detect a minimum level of support for enhancements
  * Only request JavaScript when supported
  * Fall back on non JavaScript functionality

"Cutting the mustard" is a term coined by the BBC responsive team.  The principle here is that you feature detect for a set of minimum requirements and only request and load the JavaScript when these requirements are met.  This has two advantages:

 * We can use more advanced JavaScript features knowing that they will be supported.
 * Devices that won't run our JavaScript won't even waste time downloading it.

This is a really useful technique for dealing with older browsers that have limited JavaScript support, it means you're not having to deal with a lot of compatibility problems and, because your core functionality works without JavaScript, users of these older browsers aren't missing out.

## Non JavaScript functionality
The common perception of providing non JavaScript functionality is that it's for people who have JavaScript disabled in their browsers and <a href="http://digital.cabinetoffice.gov.uk/2013/10/21/how-many-people-are-missing-out-on-javascript-enhancement/">there aren't many of them</a> so why bother?

As we've seen, having your core functionality available without JavaScript is important for more practical reasons:  It enables your users to continue to use your site when something is broken, or missing either by accident or design.

Paradoxically, by providing support when JavaScript isn't present it allows you to provide better support when it is present.
