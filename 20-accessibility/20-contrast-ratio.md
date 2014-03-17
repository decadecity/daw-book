# Understanding contrast ratio
Insufficient contrast ratio is one of the most common accessibility issues with websites and this may be due to a lack of understanding of the concerns it addresses.

## What is contrast ratio?
The colour contrast ratio of two colours is <a href="http://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef"> defined by the W3C in WCAG2.0</a> as the ratio of the relative luminescence of the foreground and background colours. This can range from a minimum of 1 (foreground and background colours are the same) to a maximum of 21 (black on white).

For compliance with WCAG2.0 AA text must have a contrast ratio of 4.5:1. There is a lower ratio required for large text (3:1) but, as large text is defined in terms of physical size, it is not possible to guarantee that text will be rendered at that size on any given device so keeping all text complaint with the 4.5:1 ratio is the best approach.

##Why is contrast ratio important?#
Whilst the use of colour is an important part of visual design there are a number of situations where users will not be able to distinguish between different colours. This doesn't just affect those who are colour blind, it is also an issue for monochrome displays, displays with poor colour reproduction, and displays viewed at an angle or in unfavourable lighting conditions.

In these situations where the hue of a colour cannot be reliably determined it is the luminosity that becomes the defining feature. If the contrast ratio of two colours is high (e.g. black on white) then, even in poor conditions, it is easy to distinguish between them. However, if the contrast ratio is too low (e.g. light blue on white) then it can be hard to distinguish between them, even in good conditions.

Whilst poor conditions or visual impairment are hard to reliably simulate, we can illustrate the effects of contrast ratio by turning colours into their greyscale equivalent.

## Examples
<i>Note: In these examples I am using <a href="http://jsbin.com/fohuy/6">a greyscale conversion based on the W3C's definition of luminescence</a> which I have chosen for illustrative purposes. There are <a href="http://dcgi.felk.cvut.cz/home/cadikm/color_to_gray_evaluation/">many methods of greyscale conversion</a> and a given monochrome display may not necessarily show these colours as the same grey. Added to which, environmental factors such as viewing angle and lighting conditions will also have an impact on how colours are perceived. Additionally there is a range in biological ability to perceive colours which is even harder to categorise. As a consequence, this choice of colours is not intended to be representative of a specific situation but to illustrate what can happen in situations where insufficient colour contrast is used.</i>

<aside>Apologies to those with difficulty perceiving colours or viewing this in monochrome, these demonstrations necessarily use colour.</aside>

### No contrast
In these examples a red and green with the same luminosity have been used.  Whilst these colours don't look particularly appealing they can still be distinguished by someone with normal colour perception in reasonable viewing conditions.

#### Contrast between foreground and background
This is the most common case for the importance of contrast, if the foreground and background don't have sufficient contrast they can be indistinguishable.

In this case we have some text that is green on red: <span style="background-color:#ff0000;color:#009400">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</span>

When reduced to greyscale the text is grey on grey: <span style="background-color:#7f7f7f;color:#7f7f7f">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</span>

Another example of this is a button: <button style="background-color:#ff0000;color:#009400">Activate!</button> which again becomes a grey box when reduced to greyscale: <button style="background-color:#7f7f7f;color:#7f7f7f">Activate!</button>

<h4>Colour used to convey meaning</h4>
Whilst relying on colour to convey meaning has wider accessibility impacts than contrast, it is still a good example of why contrast is important.

In this case we have a status indicator that shows red or green: <span style="color:#ff0000">&#9679;</span> <span style="color:#009400">&#9679;</span>

Reducing this to a greyscale representation there is no difference between the two states: <span style="color:#7f7f7f">&#9679;</span> <span style="color:#7f7f7f">&#9679;</span>

### Acceptable contrast
Here we repeat the examples above but this time a red and green with a contrast ratio better than 4.5:1 have been used.

#### Contrast between foreground and background
We still have text that is green on red: <span style="background-color:#c50000;color:#00ff00">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</span>

When reduced to greyscale the text is still grey on grey but the contrast is sufficent that they are still readable: <span style="background-color:#616161;color:#dcdcdc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</span>

Similarly applied to a button: <button style="background-color:#c50000;color:#00ff00">Activate!</button> which is still readable when reduced to greyscale: <button style="background-color:#616161;color:#dcdcdc">Activate!</button>

#### Colour used to convey meaning
Whilst using colour to convey meaning is not a good idea as the purpose of the greyscale indicators is still not apparent, at least with sufficient contrast the two states can now be distinguished from each other.

Our status indicator still shows red or green: <span style="color:#c50000">&#9679;</span> <span style="color:#00ff00">&#9679;</span>

The greyscale representation of these still doesn't communicate the meaning but does show they are different: <span style="color:#616161">&#9679;</span> <span style="color:#dcdcdc">&#9679;</span>

## Links
A similar principle applies to links. The convention on the web is to underline hyperlinks and this is what users have come to expect. By using colour - even when combined with typographical differentiation - to distinguish links without using an underline you increase the risk that they will not be recognised.

We can demonstrate this using some of the colours above:

In this example we use colour and italic text to indicate a link: <span style="color:#ff0000">This is a passage of text that contains <a href="#" style="color:#009400;text-decoration:none;font-style:italic">a link</a> within it.</span>

When reduced to greyscale the link now just looks like italicised text: <span style="color:#7f7f7f">This is a passage of text that contains <a href="#" style="color:#7f7f7f;text-decoration:none;font-style:italic">a link</a> within it.</span>

Compare this to the same example with the addition of an underline to indicate a link: <span style="color:#ff0000">This is a passage of text that contains <a href="#" style="color:#009400;text-decoration:underline;font-style:italic">a link</a> within it.</span>

When reduced to greyscale the link is still obvious within the context of a web page: <span style="color:#7f7f7f">This is a passage of text that contains <a href="#" style="color:#7f7f7f;text-decoration:underline;font-style:italic">a link</a> within it.</span>

## Conclusion
Whilst the examples here use a contrived set of colours they serve to indicate the importance of contrast ratios and conventions in making content accessible to all users on any device.
