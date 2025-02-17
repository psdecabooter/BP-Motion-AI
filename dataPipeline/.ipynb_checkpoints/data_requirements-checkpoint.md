Data Requirements for Instruction Dataset
====
# Goal
Give the model a comprehensive vision of British Parlimentary (BP) debate and BP debate motions
# Condensed Data
Json data that contains information on motions. This includes:
# Condensed data
This will only include the bare necessities

<ul>
    <li>Motion</li>
    <li>Infoslide</li>
    <li>Array of Pro Arguments (needs to be queried)
        <ul>
            <li>Premise</li>
            <li>Comparative</li>
            <li>Mechanism</li>
            <li>Impact</li>
            <li>_id</li>
        </ul>
    </li>
    <li>Array of Con Arguments (needs to be queried)
        <ul>
            <li>Premise</li>
            <li>Comparative</li>
            <li>Mechanism</li>
            <li>Impact</li>
            <li>_id</li>
        </ul>
    </li>
    <li>Instruction Types
        <ul>
            <li>Types</li>
            <li>Infoslide presence</li>
        </ul>
    </li>
</ul>

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

<ul>
    <li>Give me a resolution about x</li>
    <li>I would like arguments for x</li>
    <li>Please can I have an argument on the x side for x</li>
    <li>Can I have a motion with an info slide</li>
    <li>Give me some arguments about x</li>
    <li>Please write me a x resolution</li>
    <li>I want a resolution and some arguments for and against it</li>
    <li>Write me a resolution without an infoslide</li>
</ul>

# Output Format
Output usually looks like one or more of these things:

<ul>
    <li>A resolution</li>
    <li>An infoslide</li>
    <li>Arguments for</li>
    <li>Arguments against</li>
</ul>

# Tags
Some properties will be used to create tags

<ul>
    <li>Types</li>
    <li>Infoslide presence</li>
    <li>Category of resolution</li>
</ul>