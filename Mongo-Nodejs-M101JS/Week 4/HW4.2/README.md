<div>Suppose you have a collection called <i>tweets</i> whose documents contain information about the <i>created_at</i> time of the tweet and the user's <i>followers_count</i> at the time they issued the tweet. What can you infer from the following <i>explain</i> output?

<pre>db.tweets.find({"user.followers_count":{$gt:1000}}).sort({"created_at" : 1 }).limit(10).skip(5000).explain()
{
        "cursor" : "BtreeCursor created_at_-1 reverse",
        "isMultiKey" : false,
        "n" : 10,
        "nscannedObjects" : 46462,
        "nscanned" : 46462,
        "nscannedObjectsAllPlans" : 49763,
        "nscannedAllPlans" : 49763,
        "scanAndOrder" : false,
        "indexOnly" : false,
        "nYields" : 0,
        "nChunkSkips" : 0,
        "millis" : 205,
        "indexBounds" : {
                "created_at" : [
                        [
                                {
                                        "$minElement" : 1
                                },
                                {
                                        "$maxElement" : 1
                                }
                        ]
                ]
        },
        "server" : "localhost.localdomain:27017"
}
</pre><span><form id="inputtype_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><fieldset><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_0"><input type="checkbox" checked="" value="choice_0" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> This query performs a collection scan. </label><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_1"><input type="checkbox" checked="" value="choice_1" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> The query uses an index to determine the order in which to return result documents. </label><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_2"><input type="checkbox" value="choice_2" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> The query uses an index to determine which documents match. </label><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_3"><input type="checkbox" value="choice_3" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> The query returns 46462 documents. </label><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_4"><input type="checkbox" checked="" value="choice_4" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_4" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> The query visits 46462 documents. </label><label for="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_5"><input type="checkbox" value="choice_5" id="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1_choice_5" name="input_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1[]"> The query is a "covered index query". </label><span id="answer_i4x-10gen-M101P-problem-52aa3325e2d4232c54a18ad0_2_1"></span></fieldset></form></span></div>
