# Why should we build for the device agnostic web?
With the increasing number of devices that are connecting to the web it's simply not possible to try and target each device, device class or however else we want to try and categorise these things. By building in a device agnostic manner we are not only prepared to meet our users' expectations on their terms but we increase the reliability of our site.

I'm sure anyone who has used the internet on a device other than a traditional desktop or laptop has experienced sites that are hard to read, have some functionality broken or, even worse, have had what you were looking for removed because it's "not suitable for that type of device".  The purpose of building in a device agnostic way is to put control back into the hands of your users, allow them to access your site in the way they want.

This isn't to say that everything we build should be device agnostic, there are situations where you know that you're only going to be dealing with a restricted range of devices, there are situations where you make the decision that a certain level of feature support is required to achieve your goal and you aren't going to make allowances for devices that don't meet this. If it doesn't suit what you are doing then there's nothing wrong with not taking a device agnostic approach.

## "It depends"
The answer to the question "should I take a device agnostic approach?" is - like most questions related to the web - "it depends". If you are making a site that is available to the general public then you probably do, especially if you are likely to have a large audience.

If we take the example of a company that both sells products and provides a way of servicing those products then we can see how this can apply.

The main website that offers information about the company and the products will need to be available to as wide an audience as possible so we'll want to make sure we take the most device agnostic approach - we want this content to be accessible to everyone. We might want to have a more interesting visual design and add some interactive elements for people with more capable devices but, at this stage, we don't want to exclude anyone.

Once we move into the sales area of the site we are going to start to impose some minimum requirements. For a start we'll need to use cookies for session management and, whilst we'll not be totally reliant on JavaScript, we'll be using it a lot more to enhance the process and make it easier to complete. Whilst we might be excluding some people at this stage, the overheads of a fully device agnostic build start to become significant.

Finally, in the servicing area we are going to take the least device agnostic approach as security and ease of use become the dominant concerns. However, by this stage we know the user is one of our customers so, whilst we don't want to be taking advantage of it and using it as an excuse, they do now have a relationship with us and we can start to expect more from them in terms of using a device that meets a set of minimum requirements. In addition, we can use this relationship to offer them more support and alternative channels so they are not completely excluded.
