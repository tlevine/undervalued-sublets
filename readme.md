Finding undervalued short-term sublets
======
I search Craigslist to find low-priced short-term sublets.
And then I sublet them.

## Hypothesis
If one is going to be away from his apartment for a few weeks,
it might make sense for him to sublet his apartment for those weeks.
While you can probably find someone who would take the apartment
for approximately the right time-span, it's probably hard to find
someone who wants exactly the time-span you propose. A person
who is subletting an apartment for a specific period of duration
on the order of a month is likely to accept less than a typical
month of rent.

## Idea
All of the objects that I care to have with me regularly fit in
a suitcase and a backpack. In fact, I could probably get it down
to just a backpack; I only need the suitcase because it contains
a desk and a monitor. Thus, I am able to make full use of these
short-term sublets of externally imposed duration. So I'm going
to search Craigslist for these sublets and then sublet them.

## 3Taps Documentation
The [official documentatio](http://docs.3taps.com/) is great, except
that. Basic things like a list of the sources that 3Taps has, a list
of categories, &c. are in the [reference API](http://docs.3taps.com/reference_api.html).

[These slides](http://www.slideshare.net/devinfoley/3taps-apis)
have one example query, on slide 7.

This [PHP client](https://github.com/cookieflow/3taps-php-client)
has some vaguely helpful documentation.

### Finding sublets
The code is `RSUB`.

    $ http "http://reference.3taps.com/categories?auth_token=$APIKEY"
    ...
        {
            "code": "RSUB", 
            "group_code": "RRRR", 
            "group_name": "Real Estate", 
            "name": "Housing Sublets"
        }, 
    ...

With queries like this, you can eventually figure out the location code of interest.
But that's not too much of an issue just yet.

    http "http://reference.3taps.com/locations?auth_token=$APIKEY&state=USA-NY&level=city"

