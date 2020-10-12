var kidsWithCandies = function (candies, extraCandies) {
  const result = [];
  let max = 0;
  for (let i = 0; i < candies.length; i++) {
    if (candies[i] >= max) {
      max = candies[i];
    }
  }

  for (let i = 0; i < candies.length; i++) {
    if (candies[i] + extraCandies >= max) {
      result.push(true);
    } else {
      result.push(false);
    }
  }

  return result;
};
