# Accessibility
People often think of accessibility as being for the disabled but, done right, it will make your site more accessible for all your users regardless of ability, device and conditions.

Accessibility can seem daunting but, if you get the basics right throughout the process, it doesn't have to be a big thing.[4b]  Accessibility only really becomes a problem when you try and retro-fit it to a project at the end.

## Structure

  * Image <code>alt</code> attributes
  * Form labels
  * Tab index
  * ARIA attributes

We already have semantic markup and that's a brilliant foundation but there are a few more things that, if you get them right in your markup, will enhance your site's usability for all users - not just those who rely on assistive technology.

  * Images must have an alt attribute, even if that is null.
  * Form inputs must have labels.  Some controls - like buttons - are implicity labelled but text boxes, radio buttons, checkboxes and the like need labels.
  * Use the tabindex attribute to make sure that all your controls are accessible by keyboard navigation in a logical fashion. We'll come on to keyboard navigation later but it's not just for keyboards - the D-pad on game console controllers is normally mapped to this.  You can actually do quite a bit with the tabindex attribute so I suggest you look at the documentation.[1]
  * ARIA attributes have the promise to give a significant boost to assistive technologies but unfortunately it seems support for them in assistive technologies is slow in arriving.  It's definitely worth finding out about them and putting them into your code but don't rely on them.[2]

## Presentation

  * Contrast - 4.5:1
  * Focus highlight
  * Fixed dimensions in `em`

As with HTML, accessibility in CSS isn't just for disabled users.  An accessible site will be easier for all users to use.

Designers, if you only remember one thing from this book[3], remember this: **The minimum accessible <a href="http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef">contrast ratio</a> between foreground and background is 4.5:1**.

Don't[4c] think of this as a restriction, treat it as a challenge. The best designers I've worked with have come up with some really creative solutions that are right on this limit.[5] And remember[4], this contrast isn't just for blind people, it will make your site easy to read on monochrome screens, small screens, screens in sunlight, screens viewed at an angle - in fact most situations that aren't the nice big screen in ideal lighting you use to do your design work.

Set a prominent focus highlight.  This is essential for keyboard navigation.  This doesn't look the best for mouse and touchscreen navigation but you can use JavaScript to remove this until you detect keyboard input - the important thing is to have a prominent highlight by default. [link to explanation of this technique][6]

Don't use pixels for fixed dimensions - use ems.  This allows users to change the base or minimum font sizes and your site won't fall apart. [expand][7]

[1] What documentation? About tabindexes (any pointers for where's a good place to start?) or about consoles (is this typically in the box?)? I would unpack this more, give me examples of what I can do with it, a solid reason to bother - rather than just because you told me too in this book. Same applies to all these bullets actually. (Like, what's the point in putting 'null' in the alt attributes for an image? What kind of information should I be putting in there? A description of the image? An explanation of why I've used that image? Just stuffing it with keywords from the text?) 
[2] What are they? Can you share suggestions of where to look to find out about them?
[3] Check this update. 
[4] Quick tip from NLP - people are crap at not doing things you tell them not to do. By and large, our brains forget to process the 'Don't' bit of any message - so "Don't forget" = forget. "Don't worry" = worry. "Don't hit your sister" = tears before bedtime. (This is handy when you're marketing yourself - 'I'm a genius - don't just take my word for it, here's what previous clients say')
[4b] So the main response to this sentence is still 'accessibility is tricky and you need to pay attention to what I'm saying to get it right' - which is why I've left it as it is ;) 
[4c] I've left this one because it's nice rhetoric, and because you follow it instantly with a positive way in which it should be thought of. (Plus, it is a restriction, you just don't want them to /feel/ restricted, so it's no bad thing that their subconscious remembers to be constrained by it.)
[5] Ok - I just want you to know how clever you are here, because I suspect you don't realise... you've issued a 'challenge' to the designer, then told them what 'the best designers' do AND said that 'creative solutions... are right', and then reminded them about the restrictions, the 'limit'. A genius bit of writing for the subconscious even though you didn't realise it. You can feel smug. ;) 
[6] Don't link to it, include it. What is it, in the first place, then the how to do it. (I understand the words, but have no idea what you mean.)
[7] Yes indeed.