Data Requirements for Instruction Dataset
====
# Goal
Give the model a comprehensive vision of British Parlimentary (BP) debate and BP debate motions
# Raw Data
Json data that contains information on motions. This includes:

<ol>
    <li>_id</li>
    <li>date</li>
    <li>Region</li>
    <li>Country</li>
    <li>City</li>
    <li>Tournament</li>
    <li>Round</li>
    <li>Motion</li>
    <li>Untranslated Motion</li>
    <li>Infoslide</li>
    <li>Untranslated Infoslide</li>
    <li>Level</li>
    <li>Types</li>
    <li>Likes</li>
    <li>Dislikes</li>
    <li>URL</li>
    <li>Pro Arguments</li>
    <li>Con Arguments</li>
    <li>Complexity</li>
    <li>Slug</li>
    <li>Video URLs</li>
    <li>__v</li>
    <li>Created At</li>
</ol>

# Instruction Data
The data which the model will fine-tune on. It will be a csv structured like this:

<table>
    <tr>Question</tr>
    <tr>Answer</tr>
    <tr>Tags</tr>
</table>

<br>

# Question Format
Here are some examples of questions:

<ol>
    <li>Give me a resolution about x</li>
    <li>I would like arguments for x</li>
    <li>Please can I have an argument on the x side for x</li>
    <li>Can I have a motion with an info slide</li>
    <li>Give me some arguments about x</li>
    <li>Please write me a x resolution</li>
    <li>I want a resolution and some arguments for and against it</li>
    <li>Write me a resolution without an infoslide</li>
</ol>

# Output Format
Output usually looks like one or more of these things:

<ol>
    <li>A resolution</li>
    <li>An infoslide</li>
    <li>Arguments for</li>
    <li>Arguments against</li>
</ol>

# Tags
Some properties will be used to create tags

<ol>
    <li>Types</li>
    <li>Infoslide presence</li>
    <li>Category of resolution</li>
</ol>