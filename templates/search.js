<script src="https://cdn.jsdelivr.net/npm/fuse.js@6.0.0"></script>
<script type="text/javascript">

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
};

var fuseData = fetch('/search.json')
  .then(response => response.json())
  .catch(function (err) {
    console.log(err);
  });

const fuse = new Fuse(fuseData, options);
</script>

