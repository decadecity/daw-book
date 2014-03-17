#Coping without JavaScript

JavaScript is taking an increasingly important role in modern web sites to the point where sites that rely entirely on JavaScript are no longer uncommon.  Whilst it is tempting to assume ubiquitous and up-to-date JavaScript support when building sites it is important to conciser the experience for browsers that either have limited or no JavaScript support.  This article outlines approaches to provide content in these situations and an practical example of how to employ them.

##<code>&lt;noscript&gt;</code>
The <code>&lt;noscript&gt;</code> tag is an obvious way to deal with a lack of JavaScript support and this is certainly the way to deal with providing alternatives to functionality but it is not the most reliable way to deal with content.  The disadvantage of using the <code>&lt;noscript&gt;</code> tag for content is the lack of control we have over the display, it is entirely controlled by the browser and, according to some reports, may not be reliable in all browsers.

##CSS
If we want a reliable method of dealing with content then we need to use CSS to control the visibility.  The simplest, and most fault tolerant, way to do this is to style the content for the JavaScript disabled scenario and then use JavaScript to add a class to the `<html>` element to provide additional styling.

##Cutting The Mustard
Cutting the mustard is a phrase <a href="http://responsivenews.co.uk/post/18948466399/cutting-the-mustard">coined by the BBC</a> to describe testing for browsers that meet a certain minimum standard and, only when this standard is met, do we load the main JavaScript.  Taking a similar approach to detecting JavaScript above, we also use this test to add a class to the `<html>` element to allow us to style elements.

##SEO
When adding content in this manner it is important to conciser the SEO implications, you should try and place any content messages towards the bottom of the page if at all possible.  If the warning messages are the first thing on the page then they may appear as the snippet in Google search results.

##Bringing it all together
Shown below is an outline of an HTML page that includes practical examples of the various techniques discussed above.  You can also see the CSS techniques in action in this <a href="/static/html/pin_producer/">mini web-thing</a> (<a href="https://github.com/decadecity/pin_producer">source on GitHub</a>).

###Sample HTML page
<pre class="code">
&lt;!doctype html&gt;
&lt;html&gt;
  &lt;head&gt;
   &lt;!-- Add the CSS hook for JavaScript support. --&gt;
   &lt;script&gt;document.getElementsByTagName('html')[0].className += ' js';&lt;/script&gt;
   &lt;!-- Styling to show/hide content messages. --&gt;
   &lt;style&gt;
   .js .js-hide {
     display: none;
   }
   .legacy-warning {
     display: none;
   }
   .legacy .legacy-warning {
     display: block;
   }
   &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
   &lt;!-- Content messages in the main body. --&gt;
   &lt;div class="legacy-warning"&gt;
     &lt;p&gt;Sorry but your browser doesn't support the technologies that this application needs to run.&lt;/p&gt;
   &lt;/div&gt;
   &lt;div class="js-hide"&gt;
     &lt;p&gt;Sorry but this application requires JavaScript to be enabled in order to run.&lt;/p&gt;
   &lt;/div&gt;
   &lt;!-- Load the main JavaScript if the browser meets our minimum level. --&gt;
   &lt;script&gt;
    if ('querySelector' in document &amp;&amp; 'addEventListener' in window &amp;&amp; 'localStorage' in window) {
      document.getElementsByTagName('html')[0].className += ' ctm'; // Set CSS hook.
      // Initialise JS functionality
    } else {
      // Add a CSS hook to enable display of content messages.
      document.getElementsByTagName('html')[0].className += ' legacy';
    }
   &lt;/script&gt;
   &lt;noscript&gt;
     &lt;!-- Fallbacks for functionality. --&gt;
   &lt;/noscript&gt;
  &lt;/body&gt;
&lt;/head&gt;
</pre>

##Conclusion

 * Use <code>&lt;noscript&gt;</code> for functionality (such as analytics).
 * Use CSS hooks to provide alternative content.
 * Keep SEO implications in mind.
