#Interactions

##Touch
The touch interface should be the baseline for the UI as it gives us the best baseline for enhancement - it is easier to build up from the UI built for touch than to adapt a more traditional pointer interface to be suitable for touch, particularly as touch devices tend to translate touch events to pointer events anyway.

###Touch targets
The first key to a touch UI is targets that are easy to pick out with a finger, given the variety of device pixel densities don't get too hung up on exact physical sizes but - as ever - make sure you test on a representative sample of devices to ensure the experience is acceptable.

##Hover states
The second key to a touch interface is to avoid hover states, everything should be driven from touch/ click events.  Whilst many devices will trigger the hover state on a touch event it's not universal and the biggest problem with hover states comes when you overload items so they have different actions on hover and click - on touch devices the two events are indistinguishable.

##Keyboard
When navigating using the keyboard the important thing to remember is that it is sequential, you move from one element to the next in a set order and you need to know where you are in the sequence when navigating.

###Tabindex
By default browsers will move through focusable elements in the order in which they appear in the source but this can be overrided by use of the <a href="http://docs.webplatform.org/wiki/html/attributes/tabIndex"><code>tabindex</code></a> property.  Setting an individual tab order for each element would very quickly become tedious so it's easier to use the same tab order for items within a section as the browser will move through them in source order.  Similar to BASIC line numbering it's best to start in blocks of 10 to allow later expansion - as shown in the example below.

<pre class="code">
  &lt;a href="#"&gt;Title&lt;/a&gt;
  &lt;ol&gt;
    &lt;li tabindex="10"&gt;Item 1&lt;/li&gt;
    &lt;li tabindex="10"&gt;Item 2&lt;/li&gt;
    &lt;li tabindex="10"&gt;Item 3&lt;/li&gt;
  &lt;/ol&gt;
  &lt;button&gt;Click me!&lt;/button&gt;
  &lt;ol&gt;
    &lt;li tabindex="20"&gt;Item 4&lt;/li&gt;
    &lt;li tabindex="20"&gt;Item 5&lt;/li&gt;
    &lt;li tabindex="20"&gt;Item 6&lt;/li&gt;
  &lt;/ol&gt;
  &lt;a href="#"&gt;Footer&lt;/a&gt;
</pre>

Navigating this using the keyboard would start at "Item 1" (first item with a defined <code>tabindex</code>, lowest defined <code>tabindex</code> value, first item in mark up with lowest <code>tabindex</code>), move through "Item 2" and "Item 3" before moving on to "Item 4" (as it is the first item with the next lowest defined <code>tabindex</code>), it will then move through "Item 5" and "Item 6" before returning to the "Title" link (as it is the first item in the mark up that doesn't have a <code>tabindex</code>), the "Click me!" button and finally the "Footer" link.

<h4 id="focus">Focus</h4>
When navigating sequentially it is important to give clear feedback showing the current position.  This can be easily achieved with the <a href="http://docs.webplatform.org/wiki/css/selectors/pseudo-classes/:focus">CSS <code>:focus</code> pseudo-class</a> to define a clear visual indicator such as a contrasting outline:

<pre class="code">
*:focus {
  outline: 1px solid orange;
}
</pre>

The drawback of this is that it will show a highly visible outline on items when navigating using other methods which can be distracting.  If we set this as the default we can enhance the experience using JavaScript.

<pre class="code"><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;script&gt;
// This assumes we are using a modern browser - you'll need to <a href="/blog/2014/03/06/cutting-the-mustard">cut the mustard</a> to use this reliably.
document.querySelector('html').classList.add('js');
    &lt;/script&gt;
    &lt;style&gt;
*:focus {
  outline: 1px solid orange;
}
.js *:focus {
  outline-width: 0px;
}
.keyboard *:focus {
  outline-width: 1px;
}
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
  &lt;script&gt;
var addKeyboardHook = function () {
  document.querySelector('html').classList.add('keyboard');
  document.removeEventListener('keydown', addKeyboardHook);
};
document.addEventListener('keydown', addKeyboardHook);
  &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>

In this example we set up the obvious focus outline then use a class hook added by JavaScript to hide it.  We then listen for a <code>keydown</code> event to add in another class hook that will make the outline visible again.  This approach is heavy handed in that it takes any <code>keydown</code> event to re-show the outline, I've not found it to be a problem but you might want to do something more nuanced.

###Pointer
The mouse pointer offers the finest level of control, down to individual pixels, and allows for a hover or mouseover state that is clearly distinct from a click or activation state.  As the majority of interactions on the web have historically been mouse driven this has lead to frequent use of hover states in interfaces for a number of different tasks such as menus and tooltips.  Whilst this is clearly a useful interaction to harness it is no longer possible to rely solely on this for core functionality and it should be viewed as enhancement.  Whilst we can't currently explicitly detect pointer interfaces the best we can do is to say that if touch event support is not present then we have a pointer interface.

<pre class="code">
if (!('ontouchstart' in window)) {
  document.getElementsByTagName('html')[0].className += ' pointer';
}
</pre>

However, this is not ideal as some touch devices, such as Windows Phone 7, do not show support for touch and we want our default to be touch not pointer.

This is an ideal candidate for mobile first, server side, user agent detection backed up by positive client side feature detection.  In this scenario we add a class of <code>pointer</code> only when we positively identify a desktop browser user agent on the server and then remove it client side when we detect touch event support.

<pre class="code">
&lt;!DOCTYPE html&gt;
&lt;html class="pointer"&gt;&lt;!-- Class of pointer has been added by server.--&gt;
  &lt;head&gt;
  &lt;script&gt;
// We are using an immediately invoked, wrapped, anonymous function to keep the variable out of the global scope.
(function () {
  var html = document.getElementsByTagName('html')[0];
  if (html.className.search('pointer') &gt; -1 &amp;&amp; ('ontouchstart' in window || (typeof navigator.msMaxTouchPoints !== 'undefined' &amp;&amp; navigator.msMaxTouchPoints &gt; 0))) {
    html.className = html.className.replace('pointer', '');
  }
}());
  &lt;/script&gt;
  &lt;/head&gt;
  &lt;body/&gt;
&lt;/html&gt;
</pre>

Once we have the hook of a pointer class it can be used to add in hover states and other pointer specific UI customisations.

<pre class="code">
nav li li {
  display: none;
}

.pointer nav li:hover li {
  display: block;
}
</pre>

Whilst the <code>.pointer</code> hook might not seem necessary for <code>:hover</code> states it clearly isolates them and stops touch devices triggering them.
