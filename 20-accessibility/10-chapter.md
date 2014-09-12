# Accessibility
People often think of accessibility as being for the disabled but, done right, it will make your site more accessible for all your users regardless of ability, device and conditions.

Accessibility can seem daunting but, if you get the basics right throughout the process, you'll end up with an accessible site.  Accessibility only really becomes a problem when you try and retro-fit it to a project at the end.

## Structure

  * Image <code>alt</code> attributes
  * Form labels
  * Tab index
  * ARIA attributes

We already have semantic markup and that's a brilliant foundation but there are a few more things that, if you get them right in your markup, will enhance your site's usability for all users - not just those who rely on assistive technology.

[1]  * Images must have an alt attribute, even if that is null. Screen readers will attempt to inform users that there is an image but, without an alt attribute, what they actually read out is likely to be confusing.[2] If the alt attribute is null then screen readers will not read anything out and this is the best option for images that are decorative but do not convey any information.[3]
  * Form inputs must have labels.  Some controls - like buttons - are implicity labelled but text boxes, radio buttons, checkboxes and the like need visible labels as well since without them it is not possible for assistive technologies to determine the purpose of a field. Placeholder text is an inadequet visual substitute because, once there is data in the field, the text is removed and the purpose of the field is no longer evident.[4]
  * Use the tabindex attribute to make sure that all your controls are accessible by keyboard navigation in a logical fashion. We'll come on to keyboard navigation in [section 40/33] but it's not just for keyboards - the D-pad on game console controllers is normally mapped to this.
  * ARIA attributes have the promise to give a significant boost to assistive technologies but unfortunately it seems support for them in assistive technologies is slow in arriving. It's definitely worth finding out about them and putting them into your code but don't rely on them. More information can be found in [section 20/30].

## Presentation

  * Contrast - 4.5:1
  * Focus highlight
  * Fixed dimensions in `em`

As with HTML, accessibility in CSS isn't just for disabled users. An accessible site will be easier for all users to use.

Designers, if you only remember one thing from this book, remember this: **The minimum accessible <a href="http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef">contrast ratio</a> between foreground and background is 4.5:1**.

Don't think of this as a restriction, treat it as a challenge. The best designers I've worked with have come up with some really creative solutions that are right on this limit. And remember, this contrast isn't just for blind people, it will make your site easy to read on monochrome screens, small screens, screens in sunlight, screens viewed at an angle - in fact most situations that aren't the nice big screen in ideal lighting you use to do your design work.  More information about contrast ratio can be found in section [20/20].

[5]Set a prominent focus highlight. This is essential for keyboard navigation. It doesn't look the best for mouse and touchscreen navigation but you can use JavaScript to remove it until you detect keyboard input - the important thing is to have a prominent highlight by default. [link to explanation of this technique in section 40/33]

Don't use pixels for fixed dimensions - use ems.  This allows users to change the base or minimum font sizes and your site won't fall apart. [link to explanation if this technique in section 20/34]



[1] Why is this section in bullet points? Would be better as general paragraphs. That will require a bit more intro and linking, but at the moment it's a bit like reading notes, rather than full prose. (Also, when you're reworking it - assuming you do - take the rework through this whole section. It's a bit bullet pointy down the bottom (even though you don't actually have bullet points).)
[2] It's pedantic, but I've switched the clauses since screen readers do what they do whether there's a missing alt attribute or not.
[3] Am I actually supposed to write 'Null' into the box labelled 'alt attributes' or 'alt tag' then? Or is there a special thing that means null (like '0' perhaps?) This is more curiosity than editorial. I'd like to know I'm doing it at least vaguely right when I do stuff. (Which I'm pretty sure I'm not doing at the moment.)
[4] I've jiggled around with this point to try to make it flow better. Think it's ok, but if it doesn't sound like you then feel free to change it.