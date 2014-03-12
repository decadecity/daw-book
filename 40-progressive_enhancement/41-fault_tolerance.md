# Progressive enhancement for fault tolerance

I advocate that, to provide a solid baseline, the core functionality of your site should be available without relying on JavaScript.  The main driver behind this is fault tolerance and reliability rather than catering for the small number of users that don't have JavaScript enabled.

If the purpose of your site it to take people's money so you can get paid then you want to be able to take their money without using JavaScript.  When you add on JavaScript you can be much more efficient at taking people's money.  JavaScript is fragile, there are lots of ways in which it will break and you won't have thought of most of them.  If you aren't relying on JavaScript to take people's money then when (not if) JavaScript isn't working then you are still getting paid.

I'm not suggesting that you try and replicate all your JavaScript functionality when it's disabled, above all that's just not practical.  What you should be aiming for is being able to complete the basics - for example adding a product to a shopping cart and then checking out.  This is necessarily going to be clunky as judged by current standards and I suggest you don't spend much time on optimising this process.  What you are going to be spending the majority of your time and effort on is the enhanced JavaScript version as that is how the majority of your customers will be experiencing your site.

An additional benefit to this approach is that, as your core functionality is always available without JavaScript, you can use more advanced JavaScript features only when they are supported safe in the knowledge that you site will still work (albeit not as well) when they're not.
