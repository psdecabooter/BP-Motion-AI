import json
import random

class InstructionGenerator:
    """
    Turns the condensed data into an instruction dataset.
    All of the strings created are semi-random to improve diversity of the dataset.
    I wish python had switch statements.

    Attributes:

    Methods:
    
    """

    def __init__(self):
        pass

    def parse_motion_verb(self, motion):
        """
        Parse out the motion verb from the motion
        Examples include:
            - Believes
            - Supports
            - Regrets
            - Prefers
            - Opposes
            - Would

        Args:
            motion (dict): condensed motion format

        Returns:
            string: motion verb
        """

        if "believes" in motion['Motion'].lower():
            return 'believes'
        if 'supports' in motion['Motion'].lower():
            return 'supports'
        if 'regrets' in motion['Motion'].lower():
            return 'regrets'
        if 'prefers' in motion['Motion'].lower():
            return 'prefers'
        if 'opposes' in motion['Motion'].lower():
            return 'opposes'
        if 'would' in motion['Motion'].lower():
            return 'would'
        return ''

    def generate_motion_instruction(self, motion):
        """
        Gernerates a instruction with a question asking for a motion
        Question can include: 
            - Topics (economics, children, etc...)
            - Motion verb (regrets, would, believes that, etc...)
            - Request for infoslide
            - Request for pro arguments
            - Request for con arguments
        Answer can include:
            - Motion
            - Infoslide
            - Pro arguments
            - Con arguments
        Tags can include:
            - Types
            - Infoslide presence

        Args:
            motion (dict): condensed motion format (read data_requirements.md)

        Returns:
            string[3]: instruction data format: Question, Answer, Tags
        """

        # Store tags
        tags = []

        motion_verb = self.parse_motion_verb(motion)
        # randomize if the verb is included
        verb_rand = random.randint(0,3)
        if verb_rand != 0:
            motion_verb = ""
        else:
            tags.append(motion_verb)
            motion_verb = motion_verb + " "

        # create the string for infoslide presence
        infoslide_string = ""
        if motion['Infoslide'] != "":
            # create several possibilities for variable questions
            info_rand = random.randint(0,7) # Medium possibility
            if info_rand == 0:
                infoslide_string = "include an infoslide "
            elif info_rand == 1:
                infoslide_string = "please have an infoslide "
            elif info_rand == 2:
                infoslide_string = "with an infoslide "
            else:
                infoslide_string = ""
            tags.append('Infoslide')
        else:
            # create several possibilities
            info_rand = random.randint(0,3) # Low possibility
            if info_rand == 0:
                infoslide_string = "without an infoslide "
            else:
                infoslide_string = ""

        # create the string for topics
        topics_string = ""
        types = [x for x in motion['Types'] if x != "Infoslide"]
        if len(types) > 0:
            # randomize number of types used, weight towards using them all
            rand_length = random.randint(1,len(types)+2)
            using_topics = types if rand_length > len(types) else types[:rand_length]
            topics_string = ""
            for i in range(len(using_topics)):
                if i != 0 and i == len(using_topics)-1:
                    topics_string += ", and "
                elif i != 0:
                    topics_string += ", "
                topics_string += using_topics[i]
            tags += using_topics
                
            # create several possibilities
            topic_rand = random.randint(0,3) # high possibility
            if topic_rand == 0:
                topics_string = "about " + topics_string + " "
            elif topic_rand == 1:
                topics_string = "on the topics " + topics_string + " "
            elif topic_rand == 2:
                topics_string = "on " + topics_string + " "
            else:
                topics_string = ""
        else:
            # create several possibilities
            topic_rand = random.randint(0,3) # Low possibility
            if topic_rand == 0:
                topics_string = "on any topic "

        # create the string for pro arguments
        pro_string = ""
        if len(motion['proArguments']) > 0:
            pro_rand = random.randint(0,9) # Medium Probability
            if pro_rand == 0:
                pro_string = "include pro arguments "
            elif pro_rand == 1:
                pro_string = "include arguments for the government side "
            elif pro_rand == 2:
                pro_string = "and give me some pro arguments "
            elif pro_rand == 3:
                pro_string = "and give me some gov arguments "
            elif pro_rand == 4:
                pro_string = "please add some arguments for the government side "
            else:
                pro_string = ""
        else:
            pro_string = ""

        # create the string for con arguments
        con_string = ""
        if len(motion['conArguments']) > 0:
            con_rand = random.randint(0,9) # Medium Probability
            if con_rand == 0:
                con_string = "include con arguments "
            elif con_rand == 1:
                con_string = "include arguments for the opposition side "
            elif con_rand == 2:
                con_string = "and give me some con arguments "
            elif con_rand == 3:
                con_string = "and give me some opp arguments "
            elif con_rand == 4:
                con_string = "please add some arguments for the opposition side "
            else:
                con_string = ""
        else:
            con_string = ""
            
        # generate tags_string
        tags_string = json.dumps(tags)
        
        # generate question_string
        question_string = f"I need you to write me a motion"
        question_rand = random.randint(0,11)
        if question_rand == 0:
            question_string = f"Please give me a {motion_verb}motion {infoslide_string}{topics_string}{pro_string}{con_string}"
        elif question_rand == 1:
            question_string = f"I want a {motion_verb}motion {infoslide_string}{topics_string}{con_string}{pro_string}"
        elif question_rand == 2:
            question_string = f"{topics_string}write me a {motion_verb}motion {infoslide_string}{con_string}{pro_string}"
        elif question_rand == 3:
            question_string = f"{infoslide_string}give me a {motion_verb}motion {topics_string}{pro_string}{con_string}"
        elif question_rand == 4:
            question_string = f"{topics_string}{infoslide_string}I want a {motion_verb}motion {pro_string}{con_string}"
        elif question_rand == 6:
            question_string = f"{infoslide_string}write me a {motion_verb}motion for me {pro_string}{con_string}{topics_string}"
        elif question_rand == 7:
            question_string = f"Please write a {motion_verb}motion {con_string}{pro_string}{topics_string}{infoslide_string}"
        elif question_rand == 8:
            question_string = f"Can you give me a {motion_verb}motion {infoslide_string}{topics_string}{con_string}{pro_string}"
        elif question_rand == 9:
            question_string = f"{infoslide_string}come up with a {motion_verb}motion {topics_string}{pro_string}{con_string}"
        elif question_rand == 10:
            question_string = f"Create a {motion_verb}motion {pro_string}{topics_string}{infoslide_string}{con_string}"
        elif question_rand == 11:
            question_string = f"Make a {motion_verb}motion {infoslide_string}{topics_string}{pro_string}{con_string}"
            
        # generate answer_string
        answer_string = motion['Motion'] + ". "
        if infoslide_string != "":
            answer_string += "Infoslide: " + motion['Infoslide'] + ". "
        if pro_string != "":
            # Chose a random pro argument
            pro_index = random.randint(0,len(motion['proArguments'])-1)
            # Parse argument
            pro_arg = motion['proArguments'][pro_index]
            premise = "" if not 'Premise' in pro_arg else "Premise: " + pro_arg['Premise'] + ". "
            comparative = "" if not 'Comparative' in pro_arg else "Comparative: " + pro_arg['Comparative'] + ". "
            mechanism = "" if not 'Mechanism' in pro_arg else "Mechanism: " + pro_arg['Mechanism'] + ". "
            impact = "" if not 'Impact' in pro_arg else "Impact: " + pro_arg['Impact'] + ". "
            # Add pro Argument
            answer_string += "Here is an argument for the Government side. " + premise + comparative + mechanism + impact
        if con_string != "":
            # Chose a random pro argument
            con_index = random.randint(0,len(motion['conArguments'])-1)
            # Parse argument
            con_arg = motion['conArguments'][con_index]
            premise = "" if not 'Premise' in con_arg else "Premise: " + con_arg['Premise'] + ". "
            comparative = "" if not 'Comparative' in con_arg else "Comparative: " + con_arg['Comparative'] + ". "
            mechanism = "" if not 'Mechanism' in con_arg else "Mechanism: " + con_arg['Mechanism'] + ". "
            impact = "" if not 'Impact' in con_arg else "Impact: " + con_arg['Impact'] + ". "
            # Add pro Argument
            answer_string += "Here is an argument for the Opposition side. " + premise + comparative + mechanism + impact
        return [question_string,answer_string,tags_string]

    def generate_arguments_instruction(self, motion):
        """
        Gernerates a instruction with a question asking for arguments on a motion
        Question can include: 
            - Motion text
            - Topics (economics, children, etc...)
            - Request for pro arguments
            - Request for con arguments
        Answer can include:
            - Pro arguments
            - Con arguments
        Tags can include:
            - Types
            - Infoslide presence

        Args:
            motion (dict): condensed motion format (read data_requirements.md)

        Returns:
            string[3]: instruction data format: Question, Answer, Tags
        """
        
        # generate an instruction question if no arguments are included on the topic
        if len(motion['proArguments']) < 1 and len(motion['conArguments']) < 1:
            return generate_motion_instruction(self, motion)

        # Store tags:
        tags = []

        # Store motion verb
        motion_verb = self.parse_motion_verb(motion)
        # randomize if the verb is included
        verb_rand = random.randint(0,3)
        tags.append(motion_verb)
        motion_verb = motion_verb + " "

        # Get motion string
        motion_string = motion['Motion'] + " "

        # create the string for topics
        topics_string = ""
        types = [x for x in motion['Types'] if x != "Infoslide"]
        if len(types) > 0:
            # randomize number of types used, weight towards using them all
            rand_length = random.randint(1,len(types)+2)
            using_topics = types if rand_length > len(types) else types[:rand_length]
            topics_string = ""
            for i in range(len(using_topics)):
                if i != 0 and i == len(using_topics)-1:
                    topics_string += ", and "
                elif i != 0:
                    topics_string += ", "
                topics_string += using_topics[i]
            tags += using_topics
                
            # create several possibilities
            topic_rand = random.randint(0,2) # high possibility
            if topic_rand == 0:
                topics_string = "about " + topics_string + " "
            elif topic_rand == 1:
                topics_string = "on the topics " + topics_string + " "
            elif topic_rand == 2:
                topics_string = "on " + topics_string + " "
            else:
                topics_string = ""
        else:
            # create several possibilities
            topics_string = ""

        pro_request_string = ""
        if len(motion['proArguments']) > 0:
            pro_rand = random.randint(0,10) # High chance
            wording = "pro" if random.randint(0,4) == 0 else "government"
            # chose a random string
            if pro_rand == 0:
                pro_request_string = f"give me some {wording} arguments "
            elif pro_rand == 1:
                pro_request_string = f"create arguments for the {wording} side "
            elif pro_rand == 2:
                pro_request_string = f"I would like some {wording} arguments "
            elif pro_rand == 3:
                pro_request_string = f"could you add some {wording} arguments "
            elif pro_rand == 4:
                pro_request_string = f"make {wording} arguments "
            elif pro_rand == 5:
                pro_request_string = f"I want {wording} arguments "
            elif pro_rand == 6:
                pro_request_string = f"please write {wording} arguments "
            elif pro_rand == 7:
                pro_request_string = f"come up with arguments for the {wording} side "
            else:
                pro_request_string = ""

        con_request_string = ""
        if len(motion['conArguments']) > 0:
            con_rand = random.randint(0,10) if pro_request_string != "" else random.randint(0,7) # High chance, one side must have args
            wording = "con" if random.randint(0,4) == 0 else "opposition"
            # chose a random string
            if con_rand == 0:
                con_request_string = f"give me some {wording} arguments "
            elif con_rand == 1:
                con_request_string = f"create arguments for the {wording} side "
            elif con_rand == 2:
                con_request_string = f"I would like some {wording} arguments "
            elif con_rand == 3:
                con_request_string = f"could you add some {wording} arguments "
            elif con_rand == 4:
                con_request_string = f"make {wording} arguments "
            elif con_rand == 5:
                con_request_string = f"I want {wording} arguments "
            elif con_rand == 6:
                con_request_string = f"please write {wording} arguments "
            elif con_rand == 7:
                con_request_string = f"come up with arguments for the {wording} side "
            else:
                con_request_string = ""

        arguments_request_string = ""
        side_start = random.randint(0,1)
        if side_start == 0:
            # start with pro arguments
            if pro_request_string != "":
                arguments_request_string = pro_request_string
                if con_request_string != "":
                    # Randomize combined string
                    arg_rand = random.randint(0, 4)
                    wording = "con" if random.randint(0,4) == 0 else "opposition"
                    if arg_rand == 0:
                        arguments_request_string += "and " + con_request_string
                    else:
                        arguments_request_string += f"and for the {wording} "
            else :
                arguments_request_string = con_request_string
        else:
            # start with con arguments
            if con_request_string != "":
                arguments_request_string = con_request_string
                if pro_request_string != "":
                    # Randomize combined string
                    arg_rand = random.randint(0, 4)
                    wording = "pro" if random.randint(0,4) == 0 else "government"
                    if arg_rand == 0:
                        arguments_request_string += "and " + pro_request_string
                    else:
                        arguments_request_string += f"and for the {wording} "
            else :
                arguments_request_string = pro_request_string

        # Generate tags string
        tags_string = json.dumps(tags)
        
        # generate question_string
        question_string = ""
        question_rand = random.randint(0,8)
        if question_rand == 0:
            question_string = f"Please {arguments_request_string}for the motion {motion_string}"
        elif question_rand == 1:
            question_string = f"{arguments_request_string}for {topics_string}"
        elif question_rand == 2:
            question_string = f"{arguments_request_string}for {motion_string}"
        elif question_rand == 3:
            question_string = f"{arguments_request_string}for {motion_string}and specifically {topics_string}"
        elif question_rand == 4:
            question_string = f"{arguments_request_string}on {topics_string}"
        elif question_rand == 5:
            question_string = f"{arguments_request_string}on {motion_string}"
        elif question_rand == 6:
            question_string = f"{arguments_request_string}about the motion {motion_string}"
        elif question_rand == 7:
            question_string = f"{arguments_request_string}about {motion_string}"
        elif question_rand == 8:
            question_string = f"{arguments_request_string}on the motion {motion_string}"

        # generate answer_string
        answer_string = ""
        if pro_request_string != "":
            # Chose a random amount of pro arguments
            pro_arg_num = random.randint(1,len(motion['proArguments']))
            # Handle just one argument
            if(pro_arg_num == 1):
                answer_string += "Here is an argument for the Government side. "
            else:
                answer_string += "Here are some arguments for the Government side. "
            for pro_index in range(pro_arg_num):
                if(pro_arg_num != 1):
                    answer_string += f"Government argument {pro_index+1}. "
                # Parse argument
                pro_arg = motion['proArguments'][pro_index]
                premise = "" if not 'Premise' in pro_arg else "Premise: " + pro_arg['Premise'] + ". "
                comparative = "" if not 'Comparative' in pro_arg else "Comparative: " + pro_arg['Comparative'] + ". "
                mechanism = "" if not 'Mechanism' in pro_arg else "Mechanism: " + pro_arg['Mechanism'] + ". "
                impact = "" if not 'Impact' in pro_arg else "Impact: " + pro_arg['Impact'] + ". "
                # Add pro Argument
                answer_string += premise + comparative + mechanism + impact
        if con_request_string != "":
            # Chose a random amount of con arguments
            con_arg_num = random.randint(1,len(motion['conArguments']))
            # Handle just one argument
            if(con_arg_num == 1):
                answer_string += "Here is an argument for the Opposition side. "
            else:
                answer_string += "Here are some arguments for the Opposition side. "
            for con_index in range(con_arg_num):
                if(con_arg_num != 1):
                    answer_string += f"Opposition argument {con_index+1}. "
                # Parse argument
                con_arg = motion['conArguments'][con_index]
                premise = "" if not 'Premise' in con_arg else "Premise: " + con_arg['Premise'] + ". "
                comparative = "" if not 'Comparative' in con_arg else "Comparative: " + con_arg['Comparative'] + ". "
                mechanism = "" if not 'Mechanism' in con_arg else "Mechanism: " + con_arg['Mechanism'] + ". "
                impact = "" if not 'Impact' in con_arg else "Impact: " + con_arg['Impact'] + ". "
                # Add pro Argument
                answer_string += premise + comparative + mechanism + impact

        return [question_string,answer_string,tags_string]

    def generate_infoslide_instruction(self, motion):
        """
        Gernerates a instruction with a question asking for an infoslide for a motion
        Question must include: 
            - Motion text
            - Infoslide request
        Answer can include:
            - Motion text
            - Infoslide
        Tags can include:
            - Types
            - Infoslide presence

        Args:
            motion (dict): condensed motion format (read data_requirements.md)

        Returns:
            string[3]: instruction data format: Question, Answer, Tags
        """

        if motion['Infoslide'] == "":
            return generate_motion_instruction(self, motion) 

        # Tags 
        tags = []
        
        # Store motion verb
        motion_verb = self.parse_motion_verb(motion)
        # randomize if the verb is included
        tags.append(motion_verb)
        motion_verb = motion_verb + " "

        # Get motion string
        motion_string = motion['Motion'] + " "

        # create the string for infoslide presence
        infoslide_string = ""
        info_rand = random.randint(0,5)
        if info_rand == 0:
            infoslide_string = "create an infoslide "
        elif info_rand == 1:
            infoslide_string = "please make an infoslide "
        elif info_rand == 2:
            infoslide_string = "I would like an infoslide "
        elif info_rand == 3:
            infoslide_string = "please write an infoslide "
        elif info_rand == 4:
            infoslide_string = "come up with an infoslide "
        elif info_rand == 5:
            infoslide_string = "give me an infoslide "
        tags.append('Infoslide')

        # create the string for topics
        topics_string = ""
        types = [x for x in motion['Types'] if x != "Infoslide"]
        if len(types) > 0:
            # randomize number of types used, weight towards using them all
            rand_length = random.randint(1,len(types)+2)
            using_topics = types if rand_length > len(types) else types[:rand_length]
            topics_string = ""
            for i in range(len(using_topics)):
                if i != 0 and i == len(using_topics)-1:
                    topics_string += ", and "
                elif i != 0:
                    topics_string += ", "
                topics_string += using_topics[i]
            tags += using_topics
                
            # create several possibilities
            topic_rand = random.randint(0,2) # high possibility
            if topic_rand == 0:
                topics_string = "about " + topics_string + " "
            elif topic_rand == 1:
                topics_string = "on the topics " + topics_string + " "
            elif topic_rand == 2:
                topics_string = "on " + topics_string + " "
            else:
                topics_string = ""
        else:
            # create several possibilities
            topics_string = ""
        
        # Generate tags string
        tags_string = json.dumps(tags)

        # Generate answer string
        answer_string = f'Here is an infoslide for the motion "{motion_string}". Infoslide: {motion['Infoslide']}'

        # Generate question string
        prefix_string = "" if random.randint(0,1) == 1 else "the motion "
        question_string = ""
        question_rand = random.randint(0,2)
        if question_rand ==0:
            question_string = f"{infoslide_string}for {prefix_string}{motion_string}"
        elif question_rand == 1:
            question_string = f"{infoslide_string}about {prefix_string}{motion_string}"
        elif question_rand == 2:
            question_string = f"{infoslide_string}on {prefix_string}{motion_string}"

        return [question_string,answer_string,tags_string]
        

if __name__ == '__main__':
    instructions = InstructionGenerator()
    ex_condensed = {'Motion': 'This house regrets air', 'Infoslide': 'Air is made of gas', 'proArguments': [{'Premise': 'p', 'Comparative': 'c', 'Mechanism': 'm', 'Impact': 'i'}], 'conArguments': [{'Premise': 'np', 'Comparative': 'nc', 'Mechanism': 'nm', 'Impact': 'ni'}, {'Premise':'fingers','Comparative':'toes','Mechanism':'teeth','Impact':'YOWCH'}], 'Types': ['air', 'death', 'Infoslide']}
    print(instructions.generate_infoslide_instruction(ex_condensed))
    