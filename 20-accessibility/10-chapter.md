# Accessibility
People often think of accessibility as being for the disabled but, done right, it will make your site more accessible for all your users regardless of ability, device and conditions.

Accessibility can seem daunting but if you get the basics right throughout the process then it doesn't have to be a big thing.  Accessibility only really becomes a problem when you try and retro-fit it to a project at the end.

## Structure

  * Image <code>alt</code> attributes
  * Form labels
  * Tab index
  * ARIA roles

We already have semantic markup and that's a brilliant foundation but there are a few more things that, if you get them right in your markup, will enhance your site's usability for all users - not just those that rely on assistive technology.

  * Images must have an alt attribute, even if that is null.
  * Form inputs must have labels.  Some controls - like buttons - are implicity labelled but text boxes, radio buttons, checkboxes and the like need labels.
  * Use the tabindex attribute to make sure that all your controls are accessible by keyboard navigation in a logical fashion. We'll come on to keyboard navigation later but it's not just for keyboards - the D-pad on game console controllers is normally mapped to this.  You can actually do quite a bit with the tabindex attribute so I suggest you look at the documentation.
  * ARIA roles have the promise to give a significant boost to assistive technologies but unfortunately it seems support for them in assistive technologies is slow in arriving.  It's definitely worth finding out about them and putting them into your code but don't rely on them.

## Presentation

  * Contrast - 4.5:1
  * Focus highlight
  * Fixed dimensions in `em`

As with HTML, accessibility in CSS isn't just for disabled users.  An accessible site will be easier for all users to use.

Designers:  If you only remember one thing from this talk then remember this:  **The minimum accessible <a href="http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef">contrast ratio</a> between foreground and background is 4.5:1**.

Don't think of this as a restriction, treat it as a challenge.  The best designers I've worked with have come up with some really creative solutions that are right on this limit.  And don't forget:  this contrast isn't just for blind people, it will make your site easy to read on monochrome screens, small screens, screens in sunlight, screens viewed at an angle - in fact most situations that aren't the nice big screen in ideal lighting you use to do your design work.

Set a prominent focus highlight.  This is essential for keyboard navigation.  This doesn't look the best for mouse and touchscreen navigation but you can use JavaScript to remove this until you detect keyboard input - the important thing is to have a prominent highlight by default. [link to explanation of this technique]

Don't use pixels for fixed dimensions - use ems.  This allows users to change the base or minimum font sizes and your site won't fall apart. [expand]
