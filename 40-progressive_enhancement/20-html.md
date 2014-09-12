# HTML
The foundation of any site is the structure of the HTML but, even with a mobile first approach, all too often not enough consideration is given to this aspect of the process. Using an extensible base template is a good idea for a number of reasons but some thought should be given to how much of the site chrome (headings, footers, menus etc.) is fixed in the template.

Look at the use cases for your site, look at user journeys, look at link tracking in analytics and conduct user testing to find out how your users actually use your site. This should inform the information hierarchy for each page, which will form the linear order of the content on narrow screens. With more space, you can float and re-position content to form a richer and more consistent layout, but on a small screen you have to have the order right in the markup.[1]

You should pay most attention to the items you would not normally focus on. What is the minimum amount of content you can have in the header? Is your top level menu really the most important item in your information hierarchy? Do you even need to show the menus before the content on some pages?

## HTML
The core attributes of our HTML are that it should be clean and semantic. Getting this right gives us the best chance of it working everywhere.

Let's look at these attributes in a bit more detail:

### Clean [3]
Previously I would have said 'valid' rather than 'clean' here, however, HTML 5's validation rules are lax enough that it's not much use as a guide for where we need to be. What we're looking for is robust markup that's not going to cause problems for any browser's parser.

An advantage of HTML5 is that progressive enhancement is built it - browsers will ignore things they don't understand. This means that, providing we get the basics right, we can safely use more modern markup as long as we don't rely on it.

Correctly nesting tags should be something we do anyway - whilst you might be able to get away with overlapping tags in some browsers, you don't know how reliably an unknown browser will react.

Close all tags - even those you don't strictly have to, like line breaks, meta tags and other singleton tags. Yes, you can get away with not doing it but if you do it you don't have to "get away with it" - it's just going to work.

The same goes for quoting attributes - if you quote them, it's going to work.

What we're building up to here is that your HTML should be well formed XML. Now that probably sounds like overkill, especially as nobody really likes XML that much, but the point is that if it's well formed XML then the browser's parser doesn't have to guess about anything when it's building the DOM tree. You're not going to be caught out by how an unknown browser handles HTML it doesn't fully understand.

### Semantic
I'm not going to get into the details of exactly which element should be used to markup what content, that would take forever, everyone would disagree with me and we'd all be right. However, headings, paragraphs, lists and anchors have been around since <a href="http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt">the start of HTML</a>.  If you make sure your content is correctly marked up using these then it really should work in any browser ever made.

The new HTML5 elements - and in particular the sectioning elements such as header, footer and the like - are fine to use but we can't rely on them yet. Older browsers - and not just IE - might not recognise them, the definitions aren't all stable and I'm not sure if there's currently much out there that actually uses them. But these last two at least are likely to change so including them should help future proof your pages. My recommendation is to put them in to mark sections but then put `div`s inside them to actually hang styles and functionality from.[2] See [40/21] for more information.

It's easy to get analysis paralysis with figuring out the correct way to markup content semantically, so start with the basics to get a good foundation and focus on what the content is supposed to be rather than how it is supposed to look. Making a few dodgy decisions here and there is infinitely better than not even bothering to attempt it. If you can change the layout of your site purely by changing the CSS and without touching the markup, it's a good indication that your markup is semantic. If you can't, it will give you a good indication of where to go first to start fixing it.


_Notes_
[1] What if you're building something from scratch?
[2] You have a dangling preposition. I thought I could deal with it last time I read it - this time it annoyed me. It's up to you. Maybe next time I'll be cool with it again.
[3] This section suffers from the 'bullet point' effect. The next one doesn't.