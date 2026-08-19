#  Smart Student Performance Prediction System
## 1.Problem Statement:
- Student performance is influenced by multiple academic and behavioral factors.
- Faculty may find it difficult to identify students who are at risk at an early stage.
- A data-driven system can help predict student performance.
- The system can provide recommendations for improving student outcomes.

## 2. Proposed Solution
- Collect student-related information.
- Process the entered data.
- Use a Machine Learning model to predict performance.
- Classify students based on predicted performance.
- Generate intelligent recommendations.
- Display the results through a user-friendly Tkinter interface.

## 3. Flowchart
mermaid
flowchart TD
    A[Start] --> B[Enter Student Details]
    B --> C[Validate Input]
    C --> D[Preprocess Data]
    D --> E[ML Prediction]
    E --> F[Determine Performance Level]
    F --> G[Generate AI Recommendation]
    G --> H[Display Result]
    H --> I[End]

## 4. Project Mapping

| V-Model Stage | Smart Student Project |
|---|---|
| Requirement Analysis | Identify student performance problem |
| System Design | Design system architecture and UI |
| Implementation | Develop Python + ML application |
| Integration | Integrate UI, ML and AI |
| Testing | Test individual modules and complete system |
| Validation | Check system against requirements |
| Demonstration | Present working capstone |

## 5. Project – Modular Application Development
### Create separate functions:
- get_student_data()
- calculate_average()
- calculate_performance()
- display_result()

## 6. Requirement Analysis
### Identify the User
- Primary users may include:
- Faculty
- Academic coordinators
- Mentors
- Students
## 6.1. Functional Requirements
### The system should:
- Accept student details.
- Validate user inputs.
- Store/process student information.
- Preprocess input data.
- Apply the trained ML model.
- Predict student performance.
- Generate recommendations.
- Display results through the GUI.
- Handle invalid inputs.
- Provide a reset/clear option.

## 6.2. Non-Functional Requirements
### The application should be:
- User-friendly
- Easy to understand
- Fast in generating predictions
- Reliable
- Maintainable
- Scalable
- Secure with respect to student data
-Easy to test


## 7. User Requirement
### The user should be able to:
- Enter student information.
- Submit the information for analysis.
- View predicted performance.
- Understand the student's risk level.
- Receive improvement recommendations.

## 8. Identify System Inputs
### The initial system can use:
- Student ID
- Student name
- Attendance percentage
- Study hours per day
- Internal assessment marks
- Assignment completion percentage
- Previous academic performance
#### Example:
- Parameter	Example
- Attendance	82%
- Study Hours	4 hours/day
- Internal Marks	76%
- Assignment Completion	90%
- Previous Performance	72%

## 9. Identify System Outputs
- Performance Prediction
- Excellent
- Good
- Average
- At Risk

## 10. Additional Output
- Prediction score/probability
- Risk level
- Key factors affecting performance
-Recommended actions
#### Example:

- Prediction: Good Performance
- Risk Level: Low
- Recommendation: Maintain current study pattern and attendance

## 11. Objective

- Understand the System Design phase of the V-Model
- convert Day 1 requirements into a software architecture
- Design the workflow of the Smart Student Performance Prediction System
- Understand GUI development using Tkinter
- Create windows, frames, labels, input fields, buttons, and message boxes
- Apply pack(), grid(), and place() for layout management
- Implement event-driven programming using button callbacks, validate user inputs
- Develop a functional Tkinter prototype.

## 12. From Requirements to System Design

### Input 
- Student ID,
- Student Name
- Attendance percentage
- Study Hours
- Internal Marks
- Assignment Completion percentage
- Previous Academic Performance as inputs
  ### Processing
- validates input
- Preprocesses data
- send data to ML model,
- Generates prediction
-  Generates recommendation
  ### Outputs
-  predicted performance
-  performance category, risk level
-  Recommendation.

## 13. Proposed System Architecture

<img width="300" height="500" alt="NoteGPT-Flowchart-1787063267494" src="https://github.com/user-attachments/assets/5bb2c16b-672b-4cd9-8c97-ce604971480a" />

## 14. UI Design Requirements

The application should contain 
### 1. Student Information Section
- Student ID
- Student Name
### 2.  Academic Information Section
 - Attendance
 - Study Hours
 - Internal Marks
 - Assignment Completion
 - Previous Performance
### 3. Action Section
 - Predict Performance
 - Clear
 - Exit buttons
### 4. Result Section
 - Predicted Performance
 - Risk Level
 - Recommendation.
## 15. Using Frames
### The main window: 
- Header frames
- student information
- Academic information
- Header frame
- Results frame
## 17. Workflow
mermaid
flowchart TD
    A[User clicks Predict] --> B[Button generates event]
    B --> C[Callback function executes]
    C --> D[Python processing starts]
    
## 18. Requirements Design
<img width="691" height="543" alt="Screenshot 2026-08-19 100003" src="https://github.com/user-attachments/assets/5f4fde67-6976-42e2-be25-732338d2af99" />


