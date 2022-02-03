const { MongoClient } = require("mongodb");

(async function main() {
  const client = new MongoClient(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9"
  );
  try {
    await client.connect();
    const db = client.db("lesson");
    const books = db.collection("books");
    const bios = db.collection("bios");
    
    console.log("Exercise 1");
    console.log(await bios.findOne({ _id: 8 }));
    
    console.log("Exercise 2");
    console.log(await bios.findOne({ _id: 8 }, { _id: 1, name: 1 }));

  } catch (error) {
    console.error(`Something went wrong: ${error}`);
  } finally {
    client.close();
  }
})();
