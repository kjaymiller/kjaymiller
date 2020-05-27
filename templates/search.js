<script src="https://cdn.jsdelivr.net/npm/fuse.js@6.0.0"></script>
<script type="text/javascript">
var list = [];

fetch('/search.json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    list = data
    console.log(data)
    return data
  })
  .catch(function (err) {
    console.log(err);
  });

const options = {
  // isCaseSensitive: false,
  // includeScore: false,
  // shouldSort: true,
  // includeMatches: false,
  // findAllMatches: false,
  // minMatchCharLength: 1,
  // location: 0,
  // threshold: 0.6,
  // distance: 100,
  // useExtendedSearch: false,
  keys: [
    'title',
    '_content',
  ],
};

const fuse = new Fuse(list, options);

</script>

