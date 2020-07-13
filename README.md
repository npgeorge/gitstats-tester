# [Gitstats Tester App Link](https://gitstats-tester.herokuapp.com/)

The DS team wanted to make it easy for the web team to access endpoints, so we created this flask app to do just that. Click on the link above to check it out!

### Github Repository Example response:

(flask) bash-3.2$ curl -i https://api.github.com/repos/kubernetes/kubernetes
HTTP/1.1 200 OK
server: GitHub.com
date: Wed, 27 May 2020 18:23:07 GMT
content-type: application/json; charset=utf-8
status: 200 OK
cache-control: public, max-age=60, s-maxage=60
vary: Accept, Accept-Encoding, Accept, X-Requested-With
etag: W/"a032be8eca734b3513be7c6ccd594742"
last-modified: Wed, 27 May 2020 18:11:08 GMT
x-github-media-type: github.v3; format=json
access-control-expose-headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset
access-control-allow-origin: *
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'
X-Ratelimit-Limit: 60
X-Ratelimit-Remaining: 49
X-Ratelimit-Reset: 1590605653
Accept-Ranges: bytes
Content-Length: 6769
X-GitHub-Request-Id: C898:5597:17095:3B796:5ECEB00B

{
  "id": 20580498,
  "node_id": "MDEwOlJlcG9zaXRvcnkyMDU4MDQ5OA==",
  "name": "kubernetes",
  "full_name": "kubernetes/kubernetes",
  "private": false,
  "owner": {
    "login": "kubernetes",
    "id": 13629408,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNjI5NDA4",
    "avatar_url": "https://avatars2.githubusercontent.com/u/13629408?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/kubernetes",
    "html_url": "https://github.com/kubernetes",
    "followers_url": "https://api.github.com/users/kubernetes/followers",
    "following_url": "https://api.github.com/users/kubernetes/following{/other_user}",
    "gists_url": "https://api.github.com/users/kubernetes/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/kubernetes/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/kubernetes/subscriptions",
    "organizations_url": "https://api.github.com/users/kubernetes/orgs",
    "repos_url": "https://api.github.com/users/kubernetes/repos",
    "events_url": "https://api.github.com/users/kubernetes/events{/privacy}",
    "received_events_url": "https://api.github.com/users/kubernetes/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "html_url": "https://github.com/kubernetes/kubernetes",
  "description": "Production-Grade Container Scheduling and Management",
  "fork": false,
  "url": "https://api.github.com/repos/kubernetes/kubernetes",
  "forks_url": "https://api.github.com/repos/kubernetes/kubernetes/forks",
  "keys_url": "https://api.github.com/repos/kubernetes/kubernetes/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/kubernetes/kubernetes/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/kubernetes/kubernetes/teams",
  "hooks_url": "https://api.github.com/repos/kubernetes/kubernetes/hooks",
  "issue_events_url": "https://api.github.com/repos/kubernetes/kubernetes/issues/events{/number}",
  "events_url": "https://api.github.com/repos/kubernetes/kubernetes/events",
  "assignees_url": "https://api.github.com/repos/kubernetes/kubernetes/assignees{/user}",
  "branches_url": "https://api.github.com/repos/kubernetes/kubernetes/branches{/branch}",
  "tags_url": "https://api.github.com/repos/kubernetes/kubernetes/tags",
  "blobs_url": "https://api.github.com/repos/kubernetes/kubernetes/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/kubernetes/kubernetes/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/kubernetes/kubernetes/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/kubernetes/kubernetes/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/kubernetes/kubernetes/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/kubernetes/kubernetes/languages",
  "stargazers_url": "https://api.github.com/repos/kubernetes/kubernetes/stargazers",
  "contributors_url": "https://api.github.com/repos/kubernetes/kubernetes/contributors",
  "subscribers_url": "https://api.github.com/repos/kubernetes/kubernetes/subscribers",
  "subscription_url": "https://api.github.com/repos/kubernetes/kubernetes/subscription",
  "commits_url": "https://api.github.com/repos/kubernetes/kubernetes/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/kubernetes/kubernetes/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/kubernetes/kubernetes/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/kubernetes/kubernetes/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/kubernetes/kubernetes/contents/{+path}",
  "compare_url": "https://api.github.com/repos/kubernetes/kubernetes/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/kubernetes/kubernetes/merges",
  "archive_url": "https://api.github.com/repos/kubernetes/kubernetes/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/kubernetes/kubernetes/downloads",
  "issues_url": "https://api.github.com/repos/kubernetes/kubernetes/issues{/number}",
  "pulls_url": "https://api.github.com/repos/kubernetes/kubernetes/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/kubernetes/kubernetes/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/kubernetes/kubernetes/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/kubernetes/kubernetes/labels{/name}",
  "releases_url": "https://api.github.com/repos/kubernetes/kubernetes/releases{/id}",
  "deployments_url": "https://api.github.com/repos/kubernetes/kubernetes/deployments",
  "created_at": "2014-06-06T22:56:04Z",
  "updated_at": "2020-05-27T18:11:08Z",
  "pushed_at": "2020-05-27T18:18:46Z",
  "git_url": "git://github.com/kubernetes/kubernetes.git",
  "ssh_url": "git@github.com:kubernetes/kubernetes.git",
  "clone_url": "https://github.com/kubernetes/kubernetes.git",
  "svn_url": "https://github.com/kubernetes/kubernetes",
  "homepage": "https://kubernetes.io",
  "size": 918444,
  "stargazers_count": 66462,
  "watchers_count": 66462,
  "language": "Go",
  "has_issues": true,
  "has_projects": true,
  "has_downloads": true,
  "has_wiki": false,
  "has_pages": false,
  "forks_count": 23790,
  "mirror_url": null,
  "archived": false,
  "disabled": false,
  "open_issues_count": 2924,
  "license": {
    "key": "apache-2.0",
    "name": "Apache License 2.0",
    "spdx_id": "Apache-2.0",
    "url": "https://api.github.com/licenses/apache-2.0",
    "node_id": "MDc6TGljZW5zZTI="
  },
  "forks": 23790,
  "open_issues": 2924,
  "watchers": 66462,
  "default_branch": "master",
  "temp_clone_token": null,
  "organization": {
    "login": "kubernetes",
    "id": 13629408,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNjI5NDA4",
    "avatar_url": "https://avatars2.githubusercontent.com/u/13629408?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/kubernetes",
    "html_url": "https://github.com/kubernetes",
    "followers_url": "https://api.github.com/users/kubernetes/followers",
    "following_url": "https://api.github.com/users/kubernetes/following{/other_user}",
    "gists_url": "https://api.github.com/users/kubernetes/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/kubernetes/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/kubernetes/subscriptions",
    "organizations_url": "https://api.github.com/users/kubernetes/orgs",
    "repos_url": "https://api.github.com/users/kubernetes/repos",
    "events_url": "https://api.github.com/users/kubernetes/events{/privacy}",
    "received_events_url": "https://api.github.com/users/kubernetes/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "network_count": 23790,
  "subscribers_count": 3195
}


------- PyGithub ----------
# PyGithub list of attributes
['CHECK_AFTER_INIT_FLAG', 
'_CompletableGithubObject__complete', 
'_CompletableGithubObject__completed', 
'_GithubObject__makeSimpleAttribute', 
'_GithubObject__makeSimpleListAttribute', 
'_GithubObject__makeTransformedAttribute', 
'_Repository__create_pull', 
'_Repository__create_pull_1', 
'_Repository__create_pull_2', 
'__class__', 
'__delattr__', 
'__dict__', 
'__dir__', 
'__doc__', 
'__eq__', 
'__format__', 
'__ge__', 
'__getattribute__', 
'__gt__', 
'__hash__', 
'__init__', 
'__init_subclass__', 
'__le__', 
'__lt__', 
'__module__', 
'__ne__', 
'__new__', 
'__reduce__', 
'__reduce_ex__', 
'__repr__', 
'__setattr__', 
'__sizeof__', 
'__str__', 
'__subclasshook__', 
'__weakref__', 
'_allow_merge_commit', 
'_allow_rebase_merge', 
'_allow_squash_merge', 
'_archive_url', 
'_archived', 
'_assignees_url', 
'_blobs_url', 
'_branches_url', 
'_clone_url', 
'_collaborators_url', 
'_comments_url', 
'_commits_url', 
'_compare_url', 
'_completeIfNeeded', 
'_completeIfNotSet', 
'_contents_url', 
'_contributors_url', 
'_created_at', 
'_default_branch', 
'_delete_branch_on_merge', 
'_deployments_url',
'_description', 
'_downloads_url', 
'_events_url', 
'_fork', 
'_forks', 
'_forks_count', 
'_forks_url', 
'_full_name', 
'_git_commits_url', 
'_git_refs_url', 
'_git_tags_url', 
'_git_url', 
'_has_downloads', 
'_has_issues', 
'_has_pages', 
'_has_projects', 
'_has_wiki', 
'_headers', 
'_homepage', 
'_hooks_url', 
'_html_url', 
'_hub', 
'_id', 
'_identity', 
'_initAttributes', 
'_issue_comment_url', 
'_issue_events_url', 
'_issues_url', 
'_keys_url', 
'_labels_url', 
'_language', 
'_languages_url', 
'_legacy_convert_issue', 
'_makeBoolAttribute', 
'_makeClassAttribute', 
'_makeDatetimeAttribute', 
'_makeDictAttribute', 
'_makeDictOfStringsToClassesAttribute', 
'_makeFloatAttribute', 
'_makeIntAttribute', 
'_makeListOfClassesAttribute', 
'_makeListOfDictsAttribute', 
'_makeListOfIntsAttribute', 
'_makeListOfListOfStringsAttribute', 
'_makeListOfStringsAttribute', 
'_makeStringAttribute', 
'_makeTimestampAttribute', 
'_master_branch', 
'_merges_url', 
'_milestones_url', 
'_mirror_url', 
'_name', 
'_network_count', 
'_notifications_url', 
'_open_issues', 
'_open_issues_count', 
'_organization', 
'_owner', 
'_parent', 
'_parentUrl', 
'_permissions', 
'_private', 
'_pulls_url', 
'_pushed_at', 
'_rawData', 
'_releases_url', 
'_requester', 
'_size', 
'_source', 
'_ssh_url', 
'_stargazers_count', 
'_stargazers_url', 
'_statuses_url', 
'_storeAndUseAttributes', 
'_subscribers_count', 
'_subscribers_url', 
'_subscription_url', 
'_svn_url', 
'_tags_url', 
'_teams_url', 
'_topics', 
'_trees_url', 
'_updated_at', 
'_url', 
'_useAttributes', 
'_watchers', 
'_watchers_count', 
'add_to_collaborators', 
'allow_merge_commit', 
'allow_rebase_merge', 
'allow_squash_merge', 
'archive_url', 
'archived', 
'assignees_url', 
'blobs_url', 
'branches_url', 
'clone_url', 
'collaborators_url', 
'comments_url', 
'commits_url', 
'compare', 
'compare_url', 
'contents_url', 
'contributors_url', 
'create_deployment', 
'create_file', 
'create_fork', 
'create_git_blob', 
'create_git_commit', 
'create_git_ref', 
'create_git_release', 
'create_git_tag', 
'create_git_tag_and_release', 
'create_git_tree', 
'create_hook', 
'create_issue', 
'create_key', 
'create_label', 
'create_milestone', 
'create_project', 
'create_pull', 
'create_repository_dispatch', 
'create_source_import', 
'created_at', 
'default_branch', 
'delete', 
'delete_branch_on_merge', 
'delete_file', 
'deployments_url', 
'description', 
'disable_automated_security_fixes', 
'disable_vulnerability_alert', 
'downloads_url', 
'edit', 
'enable_automated_security_fixes', 
'enable_vulnerability_alert', 
'etag', 
'events_url', 
'fork', 
'forks', 
'forks_count', 
'forks_url', 
'full_name', 
'get__repr__', 
'get_archive_link', 
'get_assignees', 
'get_branch', 
'get_branches', 
'get_clones_traffic', 
'get_collaborator_permission', 
'get_collaborators', 
'get_comment', 
'get_comments', 
'get_commit', 
'get_commits', 
'get_contents', 
'get_contributors', 
'get_deployment', 
'get_deployments', 
'get_dir_contents', 
'get_download', 
'get_downloads', 
'get_events', 
'get_forks', 
'get_git_blob', 
'get_git_commit', 
'get_git_matching_refs', 
'get_git_ref', 
'get_git_refs', 
'get_git_tag', 
'get_git_tree', 
'get_hook', 
'get_hooks', 
'get_issue', 
'get_issues', 
'get_issues_comments', 
'get_issues_event', 
'get_issues_events', 
'get_key', 
'get_keys', 
'get_label', 
'get_labels', 
'get_languages', 
'get_latest_release', 
'get_license', 
'get_milestone', 
'get_milestones', 
'get_network_events', 
'get_notifications', 
'get_pending_invitations', 
'get_projects', 
'get_pull', 
'get_pulls', 
'get_pulls_comments', 
'get_pulls_review_comments', 
'get_readme', 
'get_release', 
'get_release_asset', 
'get_releases', 
'get_source_import', 
'get_stargazers', 
'get_stargazers_with_dates', 
'get_stats_code_frequency', 
'get_stats_commit_activity', 
'get_stats_contributors', 
'get_stats_participation', 
'get_stats_punch_card', 
'get_subscribers', 
'get_tags', 
'get_teams', 
'get_top_paths', 
'get_top_referrers', 
'get_topics', 
'get_views_traffic', 
'get_vulnerability_alert', 
'get_watchers', 
'git_commits_url', 
'git_refs_url', 
'git_tags_url', 
'git_url', 
'has_downloads', 
'has_in_assignees', 
'has_in_collaborators', 
'has_issues', 
'has_pages', 
'has_projects', 
'has_wiki', 
'homepage', 
'hooks_url', 
'html_url', 
'id', 
'issue_comment_url', 
'issue_events_url', 
'issues_url', 
'keys_url', 
'labels_url', 
'language', 
'languages_url', 
'last_modified', 
'legacy_search_issues', 
'mark_notifications_as_read', 
'master_branch', 
'merge', 
'merges_url', 
'milestones_url', 
'mirror_url', 
'name', 
'network_count', 
'notifications_url', 
'open_issues', 
'open_issues_count', 
'organization', 
'owner', 
'parent', 
'permissions', 
'private', 
'pulls_url', 
'pushed_at', 
'raw_data', 
'raw_headers', 
'releases_url', 
'remove_from_collaborators', 
'remove_invitation', 
'replace_topics', 
'setCheckAfterInitFlag', 
'size', 
'source', 
'ssh_url', 
'stargazers_count', 
'stargazers_url', 
'statuses_url', 
'subscribe_to_hub', 
'subscribers_count', 
'subscribers_url', 
'subscription_url', 
'svn_url', 
'tags_url', 
'teams_url', 
'topics', 
'trees_url', 
'unsubscribe_from_hub', 
'update', 
'update_file', 
'updated_at', 
'url', 
'watchers', 
'watchers_count']
