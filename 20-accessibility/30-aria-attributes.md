# ARIA attributes

Accessible Rich Internet Applications (ARIA) attributes allow additional information to be added to web pages to provide more information to assistive technologies.  The ARIA specification describes an overwhelming number of these attributes and support for these in assistive technologies is far from universal.  Given this lack of support, ARIA attributes should be considered an enhancement to improve accessibility rather than a way to solve more fundamental problems.

## Landmark roles
By marking up your content with semantic HTML you should have little or no need for ARIA roles that describe document structure.  There are however, some structural roles that are defined as "landmark roles" which are intended to help assistive technologies identify key navigational structures on a page that may not be identified from the semantics of the markup alone.

### Banner
The `banner` role is used to indicate content that relates to the site as a whole rather than the specific page.  This is often the header of a page that includes items such as the company logo, authentication and search.

<pre class="code"><code>&lt;header role="banner"&gt;
  &lt;img src="logo.png" alt="Company name"/&gt;
  &lt;span class="strap-line"&gt;Company strap line&lt;/span&gt;
&lt;/header&gt;</code></pre>

### Main
The `main` role is exactly analogous to the `<main>` HTML5 element, unlike other HTML5 sectioning elements - such as `<article>` which can be used more than once on a page - there should only ever be one main element on a page and this should be used to indicate the content that is key to the page.  It should be treated by assistive technologies as a "skip to content" link allowing the user to bypass any content such as banners and menus and arrive directly at the purpose of the page.  However, as support for this is limited it should not be treated as an alternative to providing a "skip to content" link, it is supplementary.  Whilst the `main` role has now superseded by the `<main>` element the role has been around for longer so, until support improves it's probably best to use both the element and the role:

`<main role="main">...</main>`

### Content information
The `contentinfo` role is similar to the `banner` role but it is used to indicate supplementary information about the page such as copyright information.

## States and properties
In a similar manner to the landmark roles, states and properties should rarely be needed if your HTML is semantic.  However, there are some that are specifically designed to provide enhanced information to assistive technologies.   Shown below are two examples but it's worth investigating the documentation to see if there are others you can make use of.

## Described by
The `aria-describedby` attribute is used to provide more textual information for an item that would normally be clear from its visual context.

For example it might be clear visually that a link to "more information" was related to the surrounding content but, taken out of context by assitive technology some additional information would help comprehension.  The value of this attribute references the ID of the item providing the description as shown below:

<pre class="code"><code>&lt;h1 id="product-name"&gt;Product Name&lt;/h1&gt;
&lt;p&gt;Product description &helip;&lt;/p&gt;
&lt;img src="product-image" alt="Product"/&gt;
&lt;a href="product-page.html" aria-describedby="product-name"&gt;more information&lt;/a&gt;</code></pre>

In this case the link is now linked so that it is clear that the more information is about the product name.

## Hidden
Whilst there are techniques for visually hiding information whilst still making it accessible to assistive technologies, the `aria-hidden` role is used to hide information from assistive technologies whilst still being visible.  This should be used with caution as an enhancement to hide visual information that has a non-visual equivalent in order to prevent duplication.

In the example shown below there is an accessible but visually hidden description of the progress indicator as well as the visual indicator:

<pre class="code"><code>&lt;span class="visually-hidden"&gt;You are on step 4 of 5&lt;/span&gt;
&lt;div class="progress-indicator" aria-hidden="true"&gt;1 2 3 &lt;span class="active"&gt;4&lt;/span&gt; 5&lt;/div&gt;</code></pre>

As the visual indicator duplicates the information in the accessible version we can mark it as hidden from assistive technologies to prevent confusion.

## How not to use ARIA attributes
As has been mentioned, if your markup is semantic then you should have little need for ARIA attributes.  The reason being that a lot of the ARAI attributes - like the `main` role - duplicate native HTML semantics.  For example the `button` role is there to designate an element allows actions when pressed.  We could use this to create a button:

`<span role="button">Press me!</span>`

We could then style this to give it the visual appearance of a button:

<pre class="code"><code>span[role=button] {
  display: block;
  padding: 0.25em;
  border-radius: 0.1em;
  border: 0.0625em solid;
}</code></pre>

However, this still isn't as good as using semantic HTML:

`<button>Press me!</button>`

##Conclusion
Whilst ARIA roles can be used to enhance accessibility, they aren't a substitute for semantic HTML.
