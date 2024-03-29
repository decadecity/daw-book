# Breaking the web
The phrase "breaking the web" is often used in discussions about web technologies and techniques. Whilst it's a simple sounding phrase it turns out that it's not actually that simple to explain.

## Accessibility
The main way I use the phrase "breaking the web" relates to breaking the accessibility of the web. When I say accessibility I'm not referring to disabled people - I'm referring to the fundamental ability to access a website. A good example of this is the use of user agent sniffing to restrict, limit or otherwise reduce access to certain browsers - typically non "mobile" devices.  Whilst this kind of thing may not necessarily be done with the intention of restricting access it's the end result that counts.

Another manifestation of this is when people try to override browsers' default behaviour because there is some aspect of it they don't like. Whilst the modified behaviour might well be considered more desirable and/or the browser's default behaviour might seem problematic, it breaks the expectation of how that browser behaves. A good example of this is using the viewport meta tag to disable zooming. This can be done to overcome more than one browser behaviour that has been considered undesirable however, as a consequence breaks a fundamental user expectation: zooming. You might argue that your site doesn't need zooming but you simply can't be aware of all the situations in which your site might be used and, in some of these cases, the ability to zoom might make the difference between the site being usable or unusable.

This type of "breaking the web" essentially comes down to a desire to exert control, but the side effect of this control is normally some form of exclusion. As much as it might make our lives easier if it were, the web is not a homogeneous environment- we should be taking the path of diversity and inclusion rather than that of specificity and exclusion.

## Not following standards
The other way I tend to use the phrase is to refer to situations where the fundamental standards of the web aren't being followed, either by accident or design. An example of this might be creating buttons from styled `<span>` elements with  an inline JavaScript event handler that navigates to a new page - the `<a>` element is designed for precisely this task, there's no need to recreate such a fundamental concept.

Also falling into this category would be an example such as using inappropriate HTTP methods. The REST standard defines a number of verbs for dealing with content - `GET` and `POST` being the most common - and these are handled in different ways.  Whilst it's by no means common, I can think of an example of a site I use regularly where `POST` is used for the majority of links between pages seemingly as a form of preventing use of the back button.

This type of "breaking the web" can come from honest ignorance but, where deliberate, comes again from a desire to exert control by using the effects of one type of behavior in a situation for which it is not designed in order to gain a non-standard behaviour.  Whilst there may appear to be a valid use case for this in a given situation, it is probably a sign that the fundamental assumptions of the design are wrong or some other - probably related - element of the standards is being used incorrectly.

## Conclusion
Whilst I accept that the phrase "breaking the web" tends to be overused - including by myself - and often for sensational effect, it can be a useful shorthand when space or time is limited, such as on Twitter.  Whilst the examples given above may seem trivial or unlikely, they hopefully serve to illustrate the kind of things I mean when I say something "breaks the web".
