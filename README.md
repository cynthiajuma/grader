# grader
Cynthia Juma
PROJECT GRADEIT!
Barnard College
12/12/2017

Project GradeIt! is an program that automatically grades an English essay based on: Length, Spelling, Simplicity and Clarity and Cognitive ability displayed. The techniques employed to achieve this include attention to length of paragraphs, sentence structure and more.

PROGRAM PART 1
I used vim to clean the html file and converted it into a plain text file because 
it was the simplest method as illustrated in the video. I manually erased the chapter headings because it was also simpler.

PROGRAM PART 2
My normalisation method is a model of method described in the Method section of the van Velzen and Garrard paper where I only calculate the mean of the segments (http://www.maneyonline.com/doi/pdfplus/10.1179/174327908X392852).

RUBRIC
My rubric used the following model:
Length: 50% of total score.
Spelling:15% of total score.
TTR:20% of total score.
Simplicity and Clarity:15% of total score.
I attached given percentage scores to their respective components with regards to how much the components affect the quality of the paper.
More work could definitely be done to diversify the rubric to cater for more types of writings
LIMITATIONS
The program may have blindspots because:
Our model pegs the richness of vocabulary to cognitive ability while richness of vocabulary is actually connected to style of writing. It is unreasonable to compare for instance, an avant garde to a realist because they use different languages to deliver their messages. Writers in different fields also use different kinds of language and jargon. While some of their works may have high TTRs, others may have a lower TTR not because there was decline in cognitive ability but because they chose to express particular ideas using particular language e.g simple words for a poem.
The model is being build to work on writing without the context in which the novels were written. this limits the effective returns because we fail to account for the basic biographic information about the authors and thus the type-token ratio would be lacking. this limits the effective returns because we fail to account for the basic biographic information about the authors and thus the type-token ratio would be lacking.
Writers use different vocabulary. Some may use simple language while others use complex words throughout their writing. This is not accounted for in the model.. 
People also have different ideas of what a “good paper” is and one’s idea of  “good paper” may not be reflected by the TTR value.

LIMITATIONS AND ASSUMPTIONS
My model assumes that essays will be in “simple”  text format - without any bullets and numbering.
The essay will be on the lines of GRE/GMAT essays.

HOW IT CAN BE IMPROVED
The function can be made smaller by getting rid of too much looping for instance by refactoring it to use intersections and unions.

LIBRARIES
The Natural Language Toolkit
enchant
string
collections
random


