import urllib.parse

class TaskQuestions(object):

    def __init__(self):
        # Tuple of query, Recency-first, COVID only
        self.task2questions = {
            'What is known about transmission, incubation, and environmental stability?': [
                ('Range of incubation periods for the disease in humans (and how this varies across age and health status) and how long individuals are contagious, even after recovery.', False, True),
                ('Prevalence of asymptomatic shedding and transmission (e.g., particularly children).', False, True),
                ('Seasonality of transmission.', False, True),
                ('Physical science of the coronavirus (e.g., charge distribution, adhesion to hydrophilic/phobic surfaces, environmental survival to inform decontamination efforts for affected areas and provide information about viral shedding).', False, True),
                ('Persistence and stability on a multitude of substrates and sources (e.g., nasal discharge, sputum, urine, fecal matter, blood).', False, True),
                ('Persistence of virus on surfaces of different materials (e,g., copper, stainless steel, plastic).', False, True),
                ('Natural history of the virus and shedding of it from an infected person', False, True),
                ('Implementation of diagnostics and products to improve clinical processes', False, True),
                ('Disease models, including animal models for infection, disease and transmission', False, True),
                ('Tools and studies to monitor phenotypic change and potential adaptation of the virus', False, True),
                ('Immune response and immunity', False, True),
                ('Effectiveness of movement control strategies to prevent secondary transmission in health care and community settings', False, True),
                ('Effectiveness of personal protective equipment (PPE) and its usefulness to reduce risk of transmission in health care and community settings', False, True),
                ('Role of the environment in transmission', False, True)],
            'What do we know about COVID-19 risk factors?': [
                ('Data on potential risks factors', False, True),
                ('Smoking, pre-existing pulmonary disease', False, True),
                ('Co-infections (determine whether co-existing respiratory/viral infections make the virus more transmissible or virulent) and other co-morbidities', False, True),
                ('Neonates and pregnant women', False, True),
                ('Socio-economic and behavioral factors to understand the economic impact of the virus and whether there were differences.', False, True),
                ('Transmission dynamics of the virus, including the basic reproductive number, incubation period, serial interval, modes of transmission and environmental factors', False, True),
                ('Severity of disease, including risk of fatality among symptomatic hospitalized patients, and high-risk patient groups', False, True),
                ('Susceptibility of populations', False, True),
                ('Public health mitigation measures that could be effective for control', False, True)],
            'What do we know about virus genetics, origin, and evolution?': [
                ('Real-time tracking of whole genomes and a mechanism for coordinating the rapid dissemination of that information to inform the development of diagnostics and therapeutics and to track variations of the virus over time.', False, True),
                ('Access to geographic and temporal diverse sample sets to understand geographic distribution and genomic differences, and determine whether there is more than one strain in circulation. Multi-lateral agreements such as the Nagoya Protocol could be leveraged.', False, True),
                ('Evidence that livestock could be infected (e.g., field surveillance, genetic sequencing, receptor binding) and serve as a reservoir after the epidemic appears to be over.', False, True),
                ('Evidence of whether farmers are infected, and whether farmers could have played a role in the origin.', False, True),
                ('Surveillance of mixed wildlife- livestock farms for SARS-CoV-2 and other coronaviruses in Southeast Asia.', False, True),
                ('Experimental infections to test host range for this pathogen.', False, True),
                ('Animal host(s) and any evidence of continued spill-over to humans', False, True),
                ('Socioeconomic and behavioral risk factors for this spill-over', False, True),
                ('Sustainable risk reduction strategies', False, True)],
            'What do we know about vaccines and therapeutics?': [
                ('Effectiveness of drugs being developed and tried to treat COVID-19 patients.', False, True),
                ('Clinical and bench trials to investigate less common viral inhibitors against COVID-19 such as naproxen, clarithromycin, and minocyclinethat that may exert effects on viral replication.', False, True),
                ('Methods evaluating potential complication of Antibody-Dependent Enhancement (ADE) in vaccine recipients.', False, True),
                ('Exploration of use of best animal models and their predictive value for a human vaccine.', False, True),
                ('Capabilities to discover a therapeutic (not vaccine) for the disease, and clinical effectiveness studies to discover therapeutics, to include antiviral agents.', False, True),
                ('Alternative models to aid decision makers in determining how to prioritize and distribute scarce, newly proven therapeutics as production ramps up. This could include identifying approaches for expanding production capacity to ensure equitable and timely distribution to populations in need.', False, True),
                ('Efforts targeted at a universal coronavirus vaccine.', False, True),
                ('Efforts to develop animal models and standardize challenge studies', False, True),
                ('Efforts to develop prophylaxis clinical studies and prioritize in healthcare workers', False, True),
                ('Approaches to evaluate risk for enhanced disease after vaccination', False, True),
                ('Assays to evaluate vaccine immune response and process development for vaccines, alongside suitable animal models [in conjunction with therapeutics]',False, True)],
            'What do we know about non-pharmaceutical interventions?': [
                ('Guidance on ways to scale up NPIs in a more coordinated way (e.g., establish funding, infrastructure and authorities to support real time, authoritative (qualified participants) collaboration with all states to gain consensus on consistent guidance and to mobilize resources to geographic areas where critical shortfalls are identified) to give us time to enhance our health care delivery system capacity to respond to an increase in cases.', False, True),
                ('Rapid design and execution of experiments to examine and compare NPIs currently being implemented. DHS Centers for Excellence could potentially be leveraged to conduct these experiments.', False, True),
                ('Rapid assessment of the likely efficacy of school closures, travel bans, bans on mass gatherings of various sizes, and other social distancing approaches.', False, True),
                ('Methods to control the spread in communities, barriers to compliance and how these vary among different populations..', False, True),
                ('Models of potential interventions to predict costs and benefits that take account of such factors as race, income, disability, age, geographic location, immigration status, housing status, employment status, and health insurance status.', False, True),
                ('Policy changes necessary to enable the compliance of individuals with limited resources and the underserved with NPIs.', False, True),
                ('Research on why people fail to comply with public health advice, even if they want to do so (e.g., social or financial costs may be too high).', False, True),
                ('Research on the economic impact of this or any pandemic. This would include identifying policy and programmatic alternatives that lessen/mitigate risks to critical government services, food distribution and supplies, access to critical household supplies, and access to health diagnoses, treatment, and needed care, regardless of ability to pay.', False, True)],
            'What has been published about medical care?': [
                ('Resources to support skilled nursing facilities and long term care facilities.', False, True),
                ('Mobilization of surge medical staff to address shortages in overwhelmed communities', False, True),
                ('Age-adjusted mortality data for Acute Respiratory Distress Syndrome (ARDS) with/without other organ failure – particularly for viral etiologies', False, True),
                ('Extracorporeal membrane oxygenation (ECMO) outcomes data of COVID-19 patients', False, True),
                ('Outcomes data for COVID-19 after mechanical ventilation adjusted for age.', False, True),
                ('Knowledge of the frequency, manifestations, and course of extrapulmonary manifestations of COVID-19, including, but not limited to, possible cardiomyopathy and cardiac arrest.', False, True),
                ('Application of regulatory standards (e.g., EUA, CLIA) and ability to adapt care to crisis standards of care level.', False, True),
                ('Approaches for encouraging and facilitating the production of elastomeric respirators, which can save thousands of N95 masks.', False, True),
                ('Best telemedicine practices, barriers and faciitators, and specific actions to remove/expand them within and across state boundaries.', False, True),
                ('Guidance on the simple things people can do at home to take care of sick people and manage disease.', False, True),
                ('Oral medications that might potentially work.', False, True),
                ('Use of AI in real-time health care delivery to evaluate interventions, risk factors, and outcomes in a way that could not be done manually.', False, True),
                ('Best practices and critical challenges and innovative solutions and technologies in hospital flow and organization, workforce protection, workforce allocation, community-based support resources, payment, and supply chain management to enhance capacity, efficiency, and outcomes.', False, True),
                ('Efforts to define the natural history of disease to inform clinical care, public health interventions, infection prevention control, transmission, and clinical trials', False, True),
                ('Efforts to develop a core clinical outcome set to maximize usability of data across a range of trials', False, True),
                ('Efforts to determine adjunctive and supportive interventions that can improve the clinical outcomes of infected patients (e.g. steroids, high flow oxygen)',False, True)],
            'What do we know about diagnostics and surveillance?': [
                ('How widespread current exposure is to be able to make immediate policy recommendations on mitigation measures. Denominators for testing and a mechanism for rapidly sharing that information, including demographics, to the extent possible. Sampling methods to determine asymptomatic disease (e.g., use of serosurveys (such as convalescent samples) and early detection of disease (e.g., use of screening of neutralizing antibodies such as ELISAs).', False, True),
                ('Efforts to increase capacity on existing diagnostic platforms and tap into existing surveillance platforms.', False, True),
                ('Recruitment, support, and coordination of local expertise and capacity (public, private—commercial, and non-profit, including academic), including legal, ethical, communications, and operational issues.', False, True),
                ('National guidance and guidelines about best practices to states (e.g., how states might leverage universities and private laboratories for testing purposes, communications to public health officials and the public).', False, True),
                ('Development of a point-of-care test (like a rapid influenza test) and rapid bed-side tests, recognizing the tradeoffs between speed, accessibility, and accuracy.', False, True),
                ('Rapid design and execution of targeted surveillance experiments calling for all potential testers using PCR in a defined area to start testing and report to a specific entity. These experiments could aid in collecting longitudinal samples, which are critical to understanding the impact of ad hoc local interventions (which also need to be recorded).', False, True),
                ('Separation of assay development issues from instruments, and the role of the private sector to help quickly migrate assays onto those devices.', False, True),
                ('Efforts to track the evolution of the virus (i.e., genetic drift or mutations) and avoid locking into specific reagents and surveillance/detection schemes.', False, True),
                ('Latency issues and when there is sufficient viral load to detect the pathogen, and understanding of what is needed in terms of biological and environmental sampling.', False, True),
                ('Use of diagnostics such as host response markers (e.g., cytokines) to detect early disease or predict severe disease progression, which would be important to understanding best clinical practice and efficacy of therapeutic interventions.', False, True),
                ('Policies and protocols for screening and testing.', False, True),
                ('Policies to mitigate the effects on supplies associated with mass testing, including swabs and reagents.', False, True),
                ('Technology roadmap for diagnostics.', False, True),
                ('Barriers to developing and scaling up new diagnostic tests (e.g., market forces), how future coalition and accelerator models (e.g., Coalition for Epidemic Preparedness Innovations) could provide critical funding for diagnostics, and opportunities for a streamlined regulatory environment.', False, True),
                ('New platforms and technology (e.g., CRISPR) to improve response times and employ more holistic approaches to COVID-19 and future diseases.', False, True),
                ('Coupling genomics and diagnostic testing on a large scale.', False, True),
                ('Enhance capabilities for rapid sequencing and bioinformatics to target regions of the genome that will allow specificity for a particular variant.', False, True),
                ('Enhance capacity (people, technology, data) for sequencing with advanced analytics for unknown pathogens, and explore capabilities for distinguishing naturally-occurring pathogens from intentional.', False, True),
                ('One Health surveillance of humans and potential sources of future spillover or ongoing exposure for this organism and future pathogens, including both evolutionary hosts (e.g., bats) and transmission hosts (e.g., heavily trafficked and farmed wildlife and domestic food and companion species), inclusive of environmental, demographic, and occupational risk factors.', False, True)],
            'What has been published about information sharing and inter-sectoral collaboration?': [
                ('Methods for coordinating data-gathering with standardized nomenclature.', False, True),
                ('Sharing response information among planners, providers, and others.', False, True),
                ('Understanding and mitigating barriers to information-sharing.', False, True),
                ('How to recruit, support, and coordinate local (non-Federal) expertise and capacity relevant to public health emergency response (public, private, commercial and non-profit, including academic).', False, True),
                ('Integration of federal/state/local public health surveillance systems.', False, True),
                ('Value of investments in baseline public health response infrastructure preparedness', False, True),
                ('Modes of communicating with target high-risk populations (elderly, health care workers).', False, True),
                ('Risk communication and guidelines that are easy to understand and follow (include targeting at risk populations’ families too).', False, True),
                ('Communication that indicates potential risk of disease to all population groups.', False, True),
                ('Misunderstanding around containment and mitigation.', False, True),
                ('Action plan to mitigate gaps and problems of inequity in the Nation’s public health capability, capacity, and funding to ensure all citizens in need are supported and can access information, surveillance, and treatment.', False, True),
                ('Measures to reach marginalized and disadvantaged populations.', False, True),
                ('Data systems and research priorities and agendas incorporate attention to the needs and circumstances of disadvantaged populations and underrepresented minorities.', False, True),
                ('Mitigating threats to incarcerated people from COVID-19, assuring access to information, prevention, diagnosis, and treatment.', False, True),
                ('Understanding coverage policies (barriers and opportunities) related to testing, treatment, and care', False, True)],
            'What has been published about ethical and social science considerations?': [
                ('Efforts to articulate and translate existing ethical principles and standards to salient issues in COVID-2019', False, True),
                ('Efforts to embed ethics across all thematic areas, engage with novel ethical issues that arise and coordinate to minimize duplication of oversight', False, True),
                ('Efforts to support sustained education, access, and capacity building in the area of ethics', False, True),
                ('Efforts to establish a team at WHO that will be integrated within multidisciplinary research and operational platforms and that will connect with existing and expanded global networks of social sciences.', False, True),
                ('Efforts to develop qualitative assessment frameworks to systematically collect information related to local barriers and enablers for the uptake and adherence to public health measures for prevention and control. This includes the rapid identification of the secondary impacts of these measures. (e.g. use of surgical masks, modification of health seeking behaviors for SRH, school closures)', False, True),
                ('Efforts to identify how the burden of responding to the outbreak and implementing public health measures affects the physical and psychological health of those providing care for Covid-19 patients and identify the immediate needs that must be addressed.', False, True),
                ('Efforts to identify the underlying drivers of fear, anxiety and stigma that fuel misinformation and rumor, particularly through social media.', False, True)],
        }

        self.example_queries = [
            ('Animal models for viral infection', False, False),
            ('Antiviral treatment for SARS clinical trials', False, False),
            ('Antivirals effective for H1N1 virus', False, False),
            ('Immunity studies for MERS', False, False),
            ('Sharing response information among planners and providers', False, False),
            ('Protecting healthcare workers', False, False),
            ('Antivirals effective for MERS', False, False),
            ('Treatments for SARS', False, False),
            ('Efficacy of zanamivir', False, False),
            ('In vitro the most effective anti-influenza drugs', False, False),
            ('Persistence of viruses on surfaces of different materials (e,g., copper, stainless steel, plastic)', False, False),
            ('Sharing response information among planners, providers, and others.', False, False),
            ('Evidence that livestock could be infected by coronavirus', False, False),
            ('In vivo MERS treatments', False, False),
            ('Protecting healthcare workers', False, False),
            ('Pregnant women coronavirus risks', False, False),
            ('Antivirals effective for H1N1', False, False),
            ('Human Coronavirus 229E background information', False, False),
            ('Animal hosts for coronavirus', False, False)
        ]


    def format_markdown_example_queries(self):
        s = "# Example Queries\n"
        for q, _, _ in self.example_queries:
            s += "* %s\n" % self.format_queries(q)
        return s

    def format_tasks(self):
        s = "# Task & Subtask Queries \n"
        for q, sti in self.task2questions.items():
            s += "## %s\n" % q
            for st, _, _ in sti:
                s += "* %s\n" % self.format_queries(st)
        return s


    def format_queries(self, q):
        return """[%s](http://kdcovid.nl/search.html?search_term=%s)""" % (q, urllib.parse.quote(q))


if __name__ == "__main__":
    tq = TaskQuestions()
    print(tq.format_markdown_example_queries())

    print(tq.format_tasks())
