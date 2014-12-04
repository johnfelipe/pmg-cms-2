class Transforms:
	convert_rules = {
		"committee": {
			"id": "id",
			"title": "name",
			"description": ["info", "about"]
		},
		"committee-meeting": {
			"id": "id",
			"title": "title",
			"description": "summary",
			"fulltext": "body",
			"date": "date",
			"committee_name": ["organisation", "name"],
			"committee_id": ["organisation", "id"],
		},
		"member": {
			"id": "id",
			"title": "name",
			"description": "bio",
			"date": "start_date",
		},
		"bill": {
			"id": "id",
			"title": "title",
			"description": "bill_code"
		},
		"hansard": {
			"id": "id",
			"title": "title",
			"fulltext": "body",
			"date": "start_date",
		},
		"briefing": {
			"id": "id",
			"title": "title",
			"description": "summary",
			"fulltext": "minutes",
			"date": "start_date",
		},
		"question_reply": {
			"id": "id",
			"title": "title",
			"fulltext": "body",
			"date": "start_date",
		},
		"tabled_committee_report": {
			"id": "id",
			"title": "title",
			"fulltext": "body",
			"date": "start_date",
		},
		"calls_for_comment": {
			"id": "id",
			"title": "title",
			"fulltext": "body",
			"date": "start_date",
		},
		"policy_document": {
			"id": "id",
			"title": "title",
			"date": "start_date",
		},
		"gazette": {
			"id": "id",
			"title": "title",
			"date": "start_date",
		},
		"daily_schedule": {
			"id": "id",
			"title": "title",
			"fulltext": "body",
			"date": "start_date",
		},
	}

	data_types = ['committee', 'committee-meeting', 'member', 'bill', 'hansard', 'briefing', 'question_reply', 'tabled_committee_report', 'calls_for_comment', 'policy_document', 'gazette', 'daily_schedule']

	model_model = { 'committee': "Organisation", 'committee-meeting': "CommitteeMeeting", 'member': "Member", 'bill': "Bill", 'hansard': "Hansard", 'briefing': "Briefing", 'question_reply': "Questions_replies", 'tabled_committee_report': "Tabled_committee_report", 'calls_for_comment': "Calls_for_comment", 'policy_document': "Policy_document", 'gazette': "Gazette", 'daily_schedule': "Daily_schedule" }