# HTML5 Elements for Legacy Browsers

Some legacy browsers, and in particular Internet Explorer prior to version 9, do not support new HTML elements such as `<article>` and `<section>`.  Here I outline a few ways of dealing with this that I have used on different projects.

## Change the Doctype

As valid HTML4 is also valid HTML5 changing the doctype shouldn't have any adverse effects for the majority of sites and, unless there is a very good technical reason not to, changing this is an easy first step towards making a site ready for HTML5 even if you aren't using any of the new elements.  If you are using the new elements then changing the doctype is a must.

## Don't use HTML5 elements

Denial is the easiest short term way of dealing with new HTML5 elements but not a <a href="http://futurefriend.ly/">future friendly</a> approach.  Whilst it is true that current technology doesn't make much use of the semantics of the new elements it is only reasonable to expect that to change so, whilst this will work for now, you aren't setting yourself up for future success.

## Use HTML5 elements with no fall back

This is a viable approach if you know that all your users will be using a browser that supports HTML5 elements.  This isn't as unreasonable as it sounds if you are building an application with <a href="http://phonegap.com/">PhoneGap</a> or <a href="http://awesomium.com/">Awesomium</a>.

This is also a viable approach if you know that the significant majority of your users will be using a browser that supports HTML5 elements and you don't care about the minority that don't.  However, this is a rather irresponsible attitude and not encouraged.

## Use HTML5 elements and the HTML5 shiv

The <a href="https://github.com/aFarkas/html5shiv/">HTML5 shiv</a> is the most often cited way to get support for HTML5 elements in older versions of <abbr title="Internet Explorer">IE</abbr> and is well tested and proven.  The main downside of this is that it requires JavaScript to be enabled, without <abbr title="JavaScript">JS</abbr> you are back to the same situation as using HTML5 elements with no fall back.  This is an acceptable approach for some projects but for those that must work with <abbr title="JavaScript">JS</abbr> disabled for accessibility, or other policy reasons, it's not viable.

## Use HTML5 elements with a class based fall back

This approach has the drawback of adding extra, semantically irrelevant, mark up to the page but has the advantage of maximum compatibility across all browsers.  To achieve this you would add an extra `<div>;` either as the parent or child of the HTML5 element and add a class that matches the HTML5 element:

<pre class="code"><code>&lt;section&gt;
  &lt;div class="section"&gt;
    &hellip;
  &lt;/div&gt;
&lt;/section&gt;</code></pre>

CSS styles are then based on the class (`.section`) rather than the element (`section`).  This has the advantage of being compatible with all browsers whilst still offering the semantics of the new elements.

## Summary

There is no right answer to which approach you should go with and there may be a case for mixing different approaches.  The approach you chose should be based on a through understanding of the project on which you are working including the browsers your users are actually using and plenty of testing.
