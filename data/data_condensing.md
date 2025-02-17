Condensing the raw data to a more useful condensed version
====

# Raw Data
Json data that contains information on motions. This includes:

<ul>
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
</ul>

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