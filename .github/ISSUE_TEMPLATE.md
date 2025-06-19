name: GitHub Actions Issue
description: Created by a GitHub Action
title: "No issue, just awesomeness"
labels: "action"
assignees:
  - {{tools.context.actor}}
body:
  - type: markdown
    attributes:
      value: Someone just pushed, oh no! Here's who did it: {{ payload.sender.login }}.
    
      tools.context.action  
      {{ tools.context.action }}
      
      tools.context.actor  
      {{ tools.context.actor }}
      
      tools.context.event  
      {{ tools.context.event }}
      
      tools.context.payload  
      {{ tools.context.payload }}
      
      tools.context.ref  
      {{ tools.context.ref }}
      
      tools.context.sha  
      {{ tools.context.sha }}
      
      tools.context.workflow  
      {{ tools.context.workflow }}
      
      tools.context.issue  
      {{ tools.context.issue }}
      
      tools.context.pullRequest  
      {{ tools.context.pullRequest }}
      
      tools.context.repo  
      {{ tools.context.repo }}
