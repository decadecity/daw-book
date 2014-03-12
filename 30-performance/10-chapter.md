# Performance

  * Set a performance budget
  * Use objective measurements (**not** times)
  * Defer non-essential items (e.g. analytics)
  * Validate using real user monitoring (RUM)

There are plenty of studies that show that the faster your site is the more people will engage with it.  Speed is also a factor in Google rankings and, thanks to a server configuration issue, I've seen that in action.

You should set a performance budget for your site to prevent it getting too slow as you add more without taking anything away.  Sticking to a budget means that when you want to add something new you have to take something out and that forces you to think about how much value the new feature really adds.

Whilst it's tempting to think of your budget in terms of time - after all that's what performance is all about - it's not practical to accurately measure time when you are building a site.  You need to define your budget in objective measurements that contribute the page speed.  The key metrics you should be focusing on are:

 * Number of HTTP requests
 * Total page weight
 * Percentage of visual rendering complete (<a href="https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index">speed index</a>)

You can make some space in your budget by deferring non-essential items.  And by essential I mean essential to your users.  Analytics is a classic example of this - whilst you might conciser them essential, your users don't care.  When was the last time you saw a slow website and thought: "I'm happy to wait for this if it means they get good analytics."

Whilst I did say don't set your budget using a time measurement, it's a good idea to measure how fast pages are actually loading for your users - this is known as <a href="http://en.wikipedia.org/wiki/Real_user_monitoring">real user monitoring</a>.  With enough data you can get a meaningful average and you can use this to ensure that changes you make to the site aren't having a negative effect on your users' load times.
