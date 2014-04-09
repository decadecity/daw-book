# Performance

  * Set a performance budget
  * Use objective measurements (**not** times)
  * Defer non-essential items (e.g. analytics)
  * Validate using real user monitoring (RUM)

There are plenty of studies[1] that show that the faster your site is the more people will engage with it. Speed is also a factor in Google rankings and, [thanks to a server configuration issue,]2 I've seen that in action. 

You should set a performance budget for your site to prevent it getting too slow as you add more without taking anything away. Sticking to a budget means that when you want to add something new you have to take something out and that forces you to think about how much value the new feature really adds.

Whilst it's tempting to think of your budget in terms of time - after all that's what performance is all about - it's not practical to accurately measure time when you're building a site. You need to define your budget in objective measurements that contribute the page speed. The key metrics to focus on are:

 * Number of HTTP requests
 * Total page weight [3]
 * Percentage of visual rendering complete (<a href="https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index">speed index</a>)

You can make some space in your budget by deferring non-essential items.  And by essential I mean essential to your users.  Analytics is a classic example of this - whilst you might conciser them essential, your users don't care.  When was the last time you saw a slow website and thought: "I'm happy to wait for this if it means they get good analytics."?

That said, it is a good idea to measure how fast pages are actually loading for your users - this is known as <a href="http://en.wikipedia.org/wiki/Real_user_monitoring">real user monitoring</a>.  With enough data you can get a meaningful average and you can use this to ensure that changes you make to the site aren't having a negative effect on your users' load times.[4]

_Notes:_
1 Give me just a couple - it makes you more credible and feeds my ability to show it to my annoying boss/client.
2 Ooo - sounds good - show/tell me more... 
3 Please expand (even if only a definintion) - what is 'weight'? how is it measured?
4 How do I do this? At what stage of trhe build should I do it? 
Throughout - try to avoid 'you should'. It's a bit preachy/dictatory whereas I think you're aiming for more conspiritorial/collaborational.
As suggested in the Homework file - I would expand this section with an explanation of what a performance budget actually is. I'd also like to see some sort of gague of what is a reasonable figure for each metric, and for the overall amount.  