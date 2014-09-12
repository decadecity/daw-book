# Building using ems [3]

The fluid grids that form a key part of responsive design use percentages to define widths so they adapt well to different viewport sizes[1]. To make sites accessible we set the base font to a percentage of the browser's base font (ideally 100%) and then size all our fonts in ems based on an assumed base font size of 16px[2]. Sizing all text relative to the base font means that when users change the base font in their browser settings to suit their requirements our styles will pick it up and adapt accordingly.

Whilst this works well for grids it won't[4] work for heights or any other situation where we need to work with 'fixed' dimensions.

## The problem with pixels
As a fixed unit, pixels might seem like they are the unit of choice for these fixed dimensions and they will certainly work up to a point. The problem comes when we start combining pixel based layout with fonts that are sized in ems. 

For example, if we set our base font size to 100% and set our heading to 2em this will, by default, result in paragraph text of 16px and heading text of 32px. If a user has changed their base font size from the default of 16px to 20px then our paragraph text will be 20px and our heading text will be 40px, maintaining the typographical relationship between the two types of text and respecting the larger font requested by the user.

If this text is within a container that has dimensions specified in pixels - for example `max-width` is commonly used to specify an upper limit on a container - then although the text is now twice as big, the container has not increased in size. If the container size is specified in ems then the container will grow in harmony with the text.[5]

## Converting from pixels to ems [7]
Similar to the `target / context` formula used when creating fluid grids[6], we can calculate the em equivalent size of a pixel dimension but in this case the context is the font size in pixels of the current context.

`max-width: 30em; /* */`

The problem with this approach is that you have to keep track of the font size of the current element, which can be a challenge - especially in more complex layouts where the font size of parent elements may have changed.

## Using rems [8]
To get round this issue of the font size of an element being liable to change the rem (root em) unit has been introduced. This is always set to the size of the font on the `<body>` element so regardless of the font size of our current context it will always be the same.

As the rem is a relatively new introduction to browsers we can't rely on it for our layouts, we still need to use a fall back.

// Work out rem fall back?




[1] To avoid having 'width' twice so close together.
[2] Why does it have to be 16px? Industry standard or just an arbitrary number? Or both?
[3] I've carved this section up quite a bit - it seemed to make more sense in this order - but if it's not what you mean, or just not how you want to say it, then change it.
[4] I know it's not formal, but I think you're writing in a 'normal' tone most of the time, so I might relax points here and there to make it fit. 
[5] These solutions seem like exactly what you'd want to happen (depending on the circumstances) - where's the problem? (As long as you know which you want)
[6] The what? I assume that is to do with setting ems for content (target) and pixels for containers (context), but I'm not 100% sure on that...
[7] I don't understand this section.
[8] I don't really understand this section either, but that's probably because it's building on the previous one. 
