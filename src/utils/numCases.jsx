export function numofcases(data){
    var numberofcases = 0;
    {
      data.map((item) => {
        item.cases.map(() => {
          numberofcases++;
        });
      });
    }

    console.log(numberofcases);
}