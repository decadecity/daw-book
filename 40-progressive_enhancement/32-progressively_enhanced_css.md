# Progressively enhanced CSS

Progressive Enhancement is a cornerstone of web development but when people talk about it they are normally talking about JavaScript. If CSS is included then it's normally in reference to cosmetic enhancements. Here's how I extend this principle deeper into CSS and layer enhancements on a larger scale, taking advantage of the <abbr title="cascading">C</abbr> in CSS.[1][2]

## Baseline presentation

Start with a baseline presentation as the main body of your CSS file (i.e. no media queries). This should include resets, colours, typography and core elements of the site.  At this stage the layout should be minimal and strictly linear - however tempted you might be, <em>do not</em> include floats or positioning yet. This is the layout that older browsers which do not support media queries will receive. Remember[3] the maxim: "The absence of media queries is the first media query."

## Narrow Screen

This is where we[4] place[?] our first media query, to enhance the presentation for browsers that support them. We use [5]<code class="code">@media <b>only</b> all</code> to target[6] these browsers and, if they bite[7], we know they have a reasonably modern CSS engine and can be relied on to handle most layout instructions corrects. Now we can start using floats and positioning to move away from the strictly linear baseline presentation. This is what you would typically think of as your first[8] mobile layout for smartphones.

## Layered Media Queries

I'm not going to say too much about this here as it is one of the cornerstones of responsive design[9] - use the code within the media queries to build out your layouts to adapt to screen size or other signal. Pay particular attention to how declarations override each other and to the 'reset' value of CSS properties as they differ.

[1] Why do you do this? 
[2] At the start of the book, you're more 'this is a useful industry standard', whereas this section is more of a 'this is how I work' bit. That's fine, but I think you want some sort of preamble that explains the industry position more, then go into your own approach, rather than just 'I do it this way' with an implication that therefore everyone else should to. (I know that's not really what you're saying, but it comes across a little like that.) As a general rule, I would recommend having as little 'I do x' stuff in here as possible. Make the book about the reader, we will assume this is how you do it, because you're the one saying this is how it should be done.
[3] Just a suggestion.
[4] You've switched into Accademic - work out which way you want this to read, collaboratively 'we can/should do x', or authoritative 'you should do y' (or if you're sticking with the 'this is how I do things' route, then this should probably be 'I do z', but I don't recommend it (see Note 2).
[5] I've removed the phrase 'media query' here because you have it so many times in such a short period of time. Ideally, I'd like you to reduce the additional instances as well. 
[6] Identify? 
[7] This is my voice not yours - put it into your language. I'm trying to join the two paragraphs and join the dots for the reader in such a way that they don't have to make logical inferences but can just agree with yours.
[8] Implication that you will end up doing more than one layout for smartphones - is that right?
[9] Err - isn't that the point of this book? Flag up where you'll actually be talking about it.