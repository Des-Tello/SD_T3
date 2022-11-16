const { query } = ajax( {
    url: 'https://en.wikipedia.org/w/api.php',
    data: {
        action: 'query',
        meta: 'tokens',
        format: 'json',
        origin: 'https://www.mediawiki.org'
    },
    xhrFields: {
        withCredentials: true
    },
    dataType: 'json'
} );

ajax( {
    url: 'https://en.wikipedia.org/w/api.php?origin=https://www.mediawiki.org',
    method: 'POST',
    data: {
        action: 'options',
        format: 'json',
        token: query.tokens.csrftoken,
        optionname: 'userjs-test',
        optionvalue: 'Hello world!'
    },
    xhrFields: {
        withCredentials: true
    },
    dataType: 'json'
} );
