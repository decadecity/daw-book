# Cutting the mustard

The phrase "cutting the mustard" was <a href="http://responsivenews.co.uk/post/18948466399/cutting-the-mustard">coined by the BBC responsive news team</a> to describe a technique of setting a minimum standard that a browser must meet in order to get an enhanced experience.  Browsers that meet this minimum standard are said to cut the mustard.

## Progressive enhancement

Cutting the mustard is a progressive enhancement technique that relies on a baseline experience that works in all browsers.  As its name suggests, the baseline experience is basic - it only uses features that are well supported in even the oldest browsers: HTML and basic CSS with no reliance on JavaScript for core functionality.

## JavaScript
The principle behind the cutting the mustard test for JavaScript is that no JavaScript is loaded unless a minimum level of feature support is present.

This is achieved with a small amount of inline JavaScript that will inject a script tag into the page if the required features are present:

<pre class="code"><code>&lt;script&gt;
if ('eventListner' in window &amp;&amp; 'querySelector' in document) {
  //Insert script.
}
&lt;/script&gt;
</code></pre>

In this case we are only loading the main JavaScript library if `window.eventListener` and `document.querySelector` are supported which means we can use these features without needing to check for support or polyfilling. This test is sufficient for <a href="/blog/2013/02/06/feature-detection-for-jquery-2">jQuery 2</a> but if your code also relies on other features then you should add these to the cutting the mustard test.

As well as knowing that any features your code requires are supported, there is the additional performance benefit that the JavaScript will not even be requested by browsers that wouldn't run it even if they did download it.

## CSS
As browsers are tolerant of CSS rules they don't understand, there is less need for a cutting the mustard test for CSS features.  It it possible to use JavaScript to detect for support of CSS features and then add a class hook to conditionally apply styles and this is an approach popularised by <a href="http://modernizr.com/">Modenizr</a>.

Whilst this approach is useful for individual features there is another approach to cutting the mustard for CSS that can be used to 'hide' more advanced CSS from older browsers by using a CSS3 media query that will only be recognised by modern browsers:

<pre class="code"><code>/* Basic CSS goes here. */

@media only all {
  /* Enhanced CSS goes here. */
}
</code></pre>

The principle here is to have a very basic, completely linear, layout that can be used by all browsers.  Those browsers that support more advanced media queries will pick up the enhanced CSS.  As this is a broad brush approach that forces you to make assumptions about what goes into the enhanced CSS based purely on media query support you should ensure that you think carefully about how you approach this and make sure you test fully in a range of browsers that cover the features you are using.
