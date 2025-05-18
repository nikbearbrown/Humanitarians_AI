# CatBot: AI-Powered Chatbot for Special Needs Cat Adoption
[Project Completed]

![CatBot Logo](catbot.png)

## Overview

CatBot is an AI-powered chatbot designed to facilitate the adoption of senior and special needs cats at The Cat Connection shelter. This project was developed by a cross-disciplinary team of students from Northeastern University's School of Engineering and D'Amore-McKim School of Business as part of the "Digital, Analytics, Technology and Automation Advanced Research Practicum" (MKTG 4606/6606).

## Project Team

- **Siddharth Dumbre** - School of Engineering, Northeastern University
- **Tanvie Sud** - D'Amore-McKim School of Business, Northeastern University
- **Shreyaan Pathak** - D'Amore-McKim School of Business, Northeastern University
- **Laasya Anantha Prasad** - D'Amore-McKim School of Business, Northeastern University
- **Nicholas Brown** - D'Amore-McKim School of Business, Northeastern University
- **Nik Bear Brown** - School of Engineering, Northeastern University
- **Debashish Ghose** - D'Amore-McKim School of Business, Northeastern University
- **Kwong Chan** - D'Amore-McKim School of Business, Northeastern University

## Problem Statement

Senior and special needs cats face significantly longer wait times for adoption in animal shelters. The Cat Connection, an all-volunteer 501(c)(3) nonprofit no-kill organization, needed an innovative solution to address several critical barriers to adoption:

1. **Information gaps**: Many potential adopters lack understanding about the care requirements and joys of adopting senior or special needs cats
2. **Matching challenges**: Finding the right personality fit between cats and adopters
3. **Post-adoption support**: Providing guidance for the critical transition period after adoption

## Solution

CatBot serves as a 24/7 digital assistant on The Cat Connection's website, providing personalized interactions with potential adopters. Key features include:

- **Educational resources** about caring for cats with specific conditions
- **Personality matching quiz** to find compatible cats based on lifestyle and preferences
- **Cost transparency** including information about medical sponsorships and support programs
- **Behavioral guidance** for the transition period after adoption
- **Volunteer and foster recruitment tools**
- **Alternative support options** for those unable to adopt

## Technical Architecture

CatBot is built using a hybrid architecture that combines:

1. **Natural Language Processing (NLP)**: Leveraging large language models for understanding and generating human-like responses
2. **Knowledge Base**: Custom-trained on special needs cat care information and resources
3. **Web Integration**: Seamless embedding within The Cat Connection's website
4. **Data Analytics**: Tracking user interactions to continuously improve responses

![Architecture Diagram](cb_collage.JPEG)

## Installation and Setup

### Prerequisites

- Voiceflow account
- A web page or any javascript compatible user interface
- API keys for chosen LLM service

### Installation and Maintainence
 - Access your website's code: Log in to your website's content management system or access your site files via FTP/SFTP.
 - Locate the appropriate files: Identify the HTML files for pages where you want CatBot to appear. Typically, you'll want to add it to all pages by editing your site's template or theme files.
 - Add the JavaScript snippet: Copy the following code and paste it just before the closing </body> tag:

```html
<script type="text/javascript">
  (function(d, t) {
    var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
    v.onload = function() {
      window.voiceflow.chat.load({
        verify: { projectID: 'YOUR_PROJECT_ID' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production',
        // Customize as needed:
        assistant: {
          position: 'right',
          sideSpacing: 20,
          bottomSpacing: 20
        }
      });
    }
    v.src = "https://cdn.voiceflow.com/widget/latest/voiceflow.bundle.js"; 
    v.async = true;
    s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```


## Usage Examples

### Educational Assistance

```
USER: "What are common health issues in senior cats?"
CATBOT: "Senior cats (10+ years) commonly experience conditions like kidney disease, arthritis, dental issues, and hyperthyroidism. Many of these conditions are manageable with proper care. Would you like information about medical support programs we offer for senior cat adopters?"
```

### Personality Matching

```
USER: "I live in a small apartment and work from home. What kind of cat would be a good fit?"
CATBOT: "Based on your living situation, a calm, mature cat who enjoys human companionship might be perfect! Several of our senior cats like Whiskers (12) and Mittens (10) thrive in quiet environments with consistent human presence. Would you like to see their profiles or take our detailed compatibility quiz?"
```

### Cost Transparency

```
USER: "How much does it cost to adopt a cat with FIV?"
CATBOT: "The adoption fee for FIV+ cats is $75, which includes vaccinations, microchipping, and spay/neuter. We also offer our Medical Support Program that provides reduced-cost veterinary care through partner clinics. Would you like details about the typical medical needs of FIV+ cats?"
```

## Research Foundation

CatBot's approach is grounded in:

1. **Behavioral economics** and consumer decision-making models
2. **Adoption barrier research** specific to special needs animals
3. **Digital marketing strategies** optimized for pet adoption
4. **Natural language processing techniques** for personalized interactions

## Impact

Since implementation on The Cat Connection's website, CatBot has:

- Increased adoption inquiries for senior and special needs cats by 45%
- Reduced volunteer time spent answering repetitive questions by approximately 25 hours weekly
- Expanded reach to potential adopters through 24/7 availability
- Improved preparation of adopters for the challenges of special needs cat care

## Contributing

We welcome contributions to improve CatBot! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Cat Connection staff and volunteers
- D'Amore-McKim School of Business AI Strategic Hub (DASH) at Northeastern University
- All the special needs cats who inspired this project

## Contact

For questions about the project, please contact:
- **Project Coordinator**: Nik Bear Brown - nikbearbrown@gmail.com
- **Technical Support**: Siddharth Dumbre - dumbre.si@northeastern.edu
- **The Cat Connection**: [Contact Page](https://thecatconnection.org/contact-us)

---

© 2025 Northeastern University | The Cat Connection
