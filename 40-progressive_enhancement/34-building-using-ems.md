# Building using ems

The fluid grids that form a key part of responsive design use percentages to define widths which means they adapt well to different viewport widths.  Whilst this works well for grids it will not work for heights and any other situation where we need to work with 'fixed' dimensions.

## The problem with pixels
As a fixed unit, pixels might seem like they are the unit of choice for these fixed dimensions and they will certainly work up to a point.  The problem comes when we start combining pixel based layout with fonts that are sized in ems.  In order to make our sites accessible we should be working with a base font that is set to a percentage of the browser's base font (ideally 100%) and then size all our fonts in ems based on an assumed base font size of 16px.  By sizing all text relative to the base font it allows users to change the base font in their browser settings to suit their requirements and our styles will pick this up.

For example, if we set our base font size to 100% and set our heading to 2em this will, by default result in paragraph text of 16px and heading text of 32px.  If a user has changed their base font size from the default of 16px to 20px then our paragraph text will be 20px and our heading text will be 40px maintaining the typographical relationship between the two types of text and respecting the larger font requested by the user.

If this text was within a container that had dimensions specified in pixels - for example `max-width` is commonly used to specify an upper limit on a container - then although the text was now twice as big, the container would not have increased in size.  If the container size was specified in ems then the container would have grown in harmony with the text.

## Converting from pixels to ems
Similar to the `target / contextt` formula used when creating fluid grids we can calculate the em equivalent size of a pixel dimension but in this case the context is the font size in pixels of the current context.

`max-width: 30em; /* */`

The problem with this approach is that the you have to keep track of the font size of the current element which can be a challenge, especially in more complex layouts where the font size of parent elements may have changed.

## Using rems
To get round this issue of the font size of an element being liable to change the rem (root em) unit has been introduced.  This is always set to the size of the font on the `<body>` element so regardless of the font size of our current context it will always be the same.

As the rem is a relatively new introduction to browsers we can't rely on it for our layouts, we still need to use a fall back.

// Work out rem fall back.




