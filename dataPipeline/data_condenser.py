import json
import requests

class DataCondenser:
    """
    Condenses the raw data and cleans it

    Attributes:
        raw_data (list of dicts): All of the raw data, formats are all specified in data_condensing.md

    Methods:
        load_data(path (int)): loads the raw json data
        condense_motion(motion (dict)): returns the condensed version of the motion
    """
    
    raw_data = None

    def __init__(self):
        pass

    def load_data(self, path):
        """
        Loads the raw data from json file

        Args:
            path (str): The path to the json file
        """
        
        # catch errors loading file
        try:
            with open(path, "r") as file:
                self.raw_data = json.load(file)
        except:
            raise ValueError("Error loading file:",str(file))

    def safe_access(self, motion, field, default):
        """
        Since the data may have missing fields, this method returns the field or default
        Prevents missing key errors

        Args:
            motion (dict): Dictionairy of a single motion from the data
            field (string): Name of the field being accessed
            default (any): Default return value if the field doesn't exist

        Returns:
            any: the field or the default value
        """
    
        if not field in motion:
            return default
        return motion[field]

    def condense_motion(self, motion):
        """
        Condenses a motion to my condensed motion format
            - Motion
            - Infoslide
            - Arguments
            - Instruction Types
        Also important for cleaning the data in the motion given

        Args:
            motion (dict): Dictionairy of a single motion from the data

        Returns:
            dict: Dictionairy of a condensed motion
        """

        condensed_motion = {}

        # If the motion field is missing, the motion is invalid
        # Cannot be fixed
        if not "Motion" in motion:
            raise ValueError("Invalid Motion")
        condensed_motion['Motion'] = motion['Motion']

        # If the infoslide field is missing, assume none existed
        infoslide = self.safe_access(motion, 'Infoslide', "")
        condensed_motion['Infoslide'] = infoslide

        # We must query arguments from debate data
        condensed_motion['proArguments'] = self.motion_to_arguments(motion, True)
        condensed_motion['conArguments'] = self.motion_to_arguments(motion, False)

        # Create the argument tags
        instruction_types = self.safe_access(motion, "Types", [])
        if infoslide != "":
            instruction_types.append("Infoslide")
        condensed_motion['Types'] = instruction_types

        # Return the condensed_motion
        return condensed_motion

    def motion_to_arguments(self, motion, isPro):
        """
        Takes a motion and queries debatedata for all of its arguments on a side

        Args:
            motion (dict): Dictionairy of a single motion from the data
            isPro (bool): True if you want pro arguments, False if you want neg arguments

        Returns:
            list: list of dicts of all arguments
        """
        pro_arguments = self.safe_access(motion, 'proArguments', [""])
        if len(pro_arguments) < 1:
            pro_arguments = [""]
        con_arguments = self.safe_access(motion, 'conArguments', [""])
        if len(con_arguments) < 1:
            con_arguments = [""]
        arg_id = pro_arguments[0] if isPro else con_arguments[0]
        payload = {
            "argumentId": [arg_id],
            "position": "Pro" if isPro else "Con",
            "motion": {
                "_id": self.safe_access(motion, '_id', ""),
                "Date": self.safe_access(motion, 'Date', ""),
                "Region": self.safe_access(motion, 'Region', ""),
                "Country": self.safe_access(motion, "Country", ""),
                "City": self.safe_access(motion, "City", ""),
                "Tournament": self.safe_access(motion, "Tournament", ""),
                "Round": self.safe_access(motion, "Round", ""),
                "Motion": self.safe_access(motion, "Motion", ""),
                "Untranslated_Motion": self.safe_access(motion, "Untranslated_Motion", ""),
                "Infoslide": self.safe_access(motion, 'Infoslide', ""),
                "Untranslated_Infoslide": self.safe_access(motion, 'Untranslated_Infoslide', ""),
                "Style": self.safe_access(motion, 'Style', ""),
                "Level": self.safe_access(motion, 'Level', ""),
                "Types": self.safe_access(motion, 'Types', []),
                "likes": self.safe_access(motion, 'likes', []),
                "dislikes": self.safe_access(motion, 'dislikes', []),
                "URL": self.safe_access(motion, 'URL', ""),
                "proArguments": self.safe_access(motion, 'proArguments', [""]),
                "conArguments": self.safe_access(motion, 'conArguments', [""]),
                "adjudicators": self.safe_access(motion, 'adjudicators', []),
                "complexity": self.safe_access(motion, 'complexity', 0),
                "slug": self.safe_access(motion, 'slug', ""),
                "videoUrls": self.safe_access(motion, 'videoUrls', []),
                "createdAt": self.safe_access(motion, 'createdAt', ""),
                "updatedAt": self.safe_access(motion, 'updatedAt', ""),
                "__v": self.safe_access(motion, '__v', 0)
            }
        }
        argument = requests.post("https://debatedata.io/api/motion/get-arguments", data=json.dumps(payload))
        if argument.status_code != 200:
            return []
        argument_object = argument.json()

        # Return the arguments
        if isPro:
            if 'proArguments' not in argument_object:
                return []
            return argument_object['proArguments']
        if 'conArguments' not in argument_object:
            return []
        return argument.json()['conArguments']

    def condense_all(self, output_path):
        """
        Condenses all motions in raw_data and puts the json in the output_path

        Args:
            output_path (string): path to the file which will hold the output
        """
        total = len(self.raw_data)
        current = 0
        condensed_motions = []
        for motion in self.raw_data:
            condensed_motions.append(self.condense_motion(motion))
            current += 1
            print(f"COUNT: {current}/{total}")
        try:
            with open(output_path, "w") as file:
                json.dump(condensed_motions, file)
        except:
            raise ValueError("Error opening file:",str(file))

if __name__ == '__main__':
    condenser = DataCondenser()
    condenser.load_data("motions.json")
    condenser.condense_all("condensed_motions.json")