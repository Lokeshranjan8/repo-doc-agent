

# @app.get("/fetchrepo")
{
  "files": [
    {
      "path": "server",
      "name": "server"
    },
    {
      "path": "server/pkg/handler/auth-controller.go",
      "name": "auth-controller.go"
    },
    {
      "path": "server/pkg/models/user.go",
      "name": "user.go"
    }
  ],
  "repo": "Lokeshranjan8/contest-reminder"
}

#http://localhost:8081/judge/docker-files

{
  "repo": "Lokeshranjan8/contest-tracker",
  "files": [
    { "name": "Topics.js", "path": "server/utils/Topics.js" },
    { "name": "docker-compose.yml", "path": "docker-compose.yml" },
    { "name": "Dockerfile", "path": "backend/Dockerfile" },
    { "name": "README.md", "path": "README.md" }
  ],
  "readme_imp": []
}



#  ASMIT  -TEST THIS endpoint

#  http://localhost:8081/fetchrepo?repo_url=https://github.com/Lokeshranjan8/contest-reminder
# correct this path   
"readme_imp": [
    "docker-compose.yml",
    "package.json",
    "Dockerfile"
  ]
} 
# llm not returning expected result we needed 

# chanegs required in node1.py line 24-prompt mistakes correct it make it universal 